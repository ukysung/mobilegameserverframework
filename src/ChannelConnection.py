
import g
import asyncio
import struct

import msg_header
from Channel import channel_add_player, channel_remove_player

@asyncio.coroutine
def handle_message_no_1(req_msg_type, req_msg_body):
	print('message_no_1')
	#return (0, req_msg_body)
	return req_msg_body

g.handlers[1] = handle_message_no_1

import time
@asyncio.coroutine
def handle_outgoing():
	while not g.outgoing.empty():
		print('handl_n')
		d = yield from g.outgoing.get()

	time.sleep(1)
	asyncio.Task(handle_outgoing())

class ChannelConnection(asyncio.Protocol):
	def __init__(self):
		self.timeout_sec = 1800.0
		self.msg_buffer = b''

	def connection_made(self, transport):
		self.transport = transport
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)

		g.sess_idx += 1
		if g.sess_idx == 100000:
			g.sess_idx = 1

		g.sessions[g.sess_idx] = self
		g.incoming.put([1, g.sess_idx])

	def data_received(self, data):
		self.h_timeout.cancel()
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)

		print(data)
		return

		#self.msg_buffer += data
		g.incoming.put(data)
		return

		msg_header_offset = 0
		while len(self.msg_buffer) >= (msg_header_offset + msg_header.size):
			msg_body_offset = msg_header_offset + msg_header.size
			(msg_type, msg_size) = struct.unpack('ii', self.msg_buffer[msg_header_offset:msg_body_offset])

			msg_end_offset = msg_header_offset + msg_size
			if len(self.msg_buffer) < msg_end_offset:
				break

			msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
			msg_header_offset = msg_end_offset

			asyncio.Task(self.handle_received(msg_type, msg_body))

		self.msg_buffer = self.msg_buffer[msg_header_offset:]

		#print(data)
		#for conn in connections:
			#if conn is not self:
				#conn.transport.write(ack)

	def eof_received(self):
		pass

	def connection_lost(self, ex):
		self.h_timeout.cancel()
		#connections.remove(self)

	def connection_timed_out(self):
		self.transport.close()

