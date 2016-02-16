
import logging
import struct
import asyncio

def test():
	return ''

handlers = {
	1: test,
}

'''
struct
{
	int32_t msg_type; // 4 bytes
	int32_t msg_size; // 4 bytes
}
// totally 8 bytes
'''
msg_head_size = 8

@asyncio.coroutine
def request_handler(req_msg_type, req_msg_body):
	if handlers[req_msg_type] is None:
		return ''

	(ack_msg_type, ack_msg_body) = handlers[req_msg_type](req_msg_body)
	return struct.pack('ii', ack_msg_type, msg_head_size + len(ack_msg_body)) + ack_msg_body

def packet_handler(reader, writer):
	while True:
		req_msg_head = yield from reader.read(msg_head_size)
		if len(req_msg_head) == 0:
			break

		(req_msg_type, req_msg_size) = struct.unpack('ii', req_msg_head)
		req_msg_body_size = req_msg_size - msg_head_size
		if req_msg_body_size <= 0 or req_msg_body_size > 8192:
			break

		req_msg_body = yield from reader.read(req_msg_body_size)
		if len(req_msg_body) == 0:
			break

		ack = yield from request_handler(req_msg_type, req_msg_body)
		if len(ack) == 0:
			break

		writer.write(ack)

clients = {}
def connection_handler(reader, writer):
	task = asyncio.Task(packet_handler(reader, writer))
	clients[task] = (reader, writer)

	def task_done(task):
		del clients[task]

	task.add_done_callback(task_done)

def main():
	loop = asyncio.get_event_loop()
	server = loop.run_until_complete(asyncio.start_server(connection_handler, 'localhost', 59999))

	try:
		loop.run_forever()

	except KeyboardInterrupt:
		pass

	server.close()
	loop.close()

if __name__ == '__main__':
	main()
