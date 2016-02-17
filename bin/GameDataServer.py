
import struct
import logging, logging.handlers
import json
import asyncio
import sys
import signal

import google.protobuf

'''
struct
{
	int32_t msg_type; // 4 bytes
	int32_t msg_size; // 4 bytes
}
// totally 8 bytes
'''
msg_head_size = 8

log = None
cfg = {}
mst = {}

@asyncio.coroutine
def handle_message_no_1():
	return ''

players = {}
handlers = {
	1:handle_message_no_1,
}

@asyncio.coroutine
def request_handler(req_msg_type, req_msg_body):
	if handlers[req_msg_type] is None:
		return ''

	(ack_msg_type, ack_msg_body) = yield from handlers[req_msg_type](req_msg_type, req_msg_body)
	return struct.pack('ii', ack_msg_type, head_size + len(ack_msg_body), 0, 0) + ack_msg_body

@asyncio.coroutine
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
		writer.write(ack)

		# this enables us to have flow control in our connection
		writer.drain()

def connection_handler(reader, writer):
	task = asyncio.Task(request_handler(reader, writer))
	players[task] = (reader, writer)

	def task_done(task):
		del players[task]

	task.add_done_callback(task_done)

def main():
	if len(sys.argv) < 2:
		print('Usage: sudo python3 ./GameDataServer.py develop 00')
		sys.exit()

	phase = sys.argv[1]
	server_id = sys.argv[2]

	# cfg
	with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
		cfg = json.loads(cfg_file.read())

	# log
	log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
	log_handler = logging.handlers.TimedRotatingFileHandler('../log/game_data_server_log_' + server_id + '.csv', when='M', interval=1)
	log_handler.setFormatter(log_formatter)

	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	log.addHandler(log_handler)

	# server
	loop = asyncio.get_event_loop()
	server = loop.run_until_complete(asyncio.start_server(connection_handler, 'localhost', 50001))

	try:
		loop.run_forever()

	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

if __name__ == '__main__':
	main()

