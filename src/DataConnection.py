
import g
import asyncio
import struct

import msg_header

@asyncio.coroutine
def handle_message_no_1(req_msg_type, req_msg_body):
	print('message_no_1')
	return b'kkkk'

g.handlers[1] = handle_message_no_1

class DataConnection(asyncio.Protocol):
	def __init__(self):
		g.log.info('haha')
		self.timeout_sec = 600.0
		self.msg_buffer = b''

	@asyncio.coroutine
	def data_received_impl(self, req_msg_type, req_msg_body):
		print('handle_received')
		if g.handlers[req_msg_type] is None:
			return

		#(ack_msg_type, ack_msg_body) = yield from g.handlers[req_msg_type](req_msg_type, req_msg_body)
		kkkk = yield from g.handlers[req_msg_type](req_msg_type, req_msg_body)
		#ack = struct.pack('ii', ack_msg_type, msg_head_size + len(ack_msg_body)) + ack_msg_body

		#self.transport.write(ack)
		self.transport.write(kkkk)

	def connection_made(self, transport):
		self.transport = transport
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)
		g.sessions.append(self)

	def data_received(self, data):
		self.h_timeout.cancel()
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)

		self.msg_buffer += data
		if len(self.msg_buffer) > 8192:
			return
		print(self.msg_buffer)
		print('asyncio task')
		asyncio.Task(self.data_received_impl(1, self.msg_buffer))
		return

		msg_head_offset = 0

		while len(self.msg_buffer) >= (msg_head_offset + msg_head_size):
			msg_body_offset = msg_head_offset + msg_head_size
			(msg_type, msg_size) = struct.unpack('ii', self.msg_buffer[msg_head_offset:msg_body_offset])

			msg_end_offset = msg_head_offset + msg_size
			if len(self.msg_buffer) < msg_end_offset:
				break

			msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
			msg_head_offset = msg_end_offset

			asyncio.Task(self.handle_received(msg_type, msg_body))

		self.msg_buffer = self.msg_buffer[msg_head_offset:]

	def eof_received(self):
		pass

	def connection_lost(self, ex):
		self.h_timeout.cancel()
		g.sessions.remove(self)

	def connection_timed_out(self):
		self.transport.close()

