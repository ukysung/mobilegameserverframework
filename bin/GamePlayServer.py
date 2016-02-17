
import struct
import logging, logging.handlers
import json
import asyncio
import sys
import signal

import google.protobuf
import game_client.CLIENT_GAME_NET_PROTOCOL_RESULT_pb2
import game_client.CLIENT_GAME_NET_PROTOCOL_pb2
import db_packet.db_msg_pb2
import db_table.db_table_pb2

'''
struct
{
	int32_t msg_type; // 4 bytes
	int32_t msg_size; // 4 bytes
}
// totally 8 bytes
'''
msg_head_size = 6

log = None
cfg = {}
mst = {}
handlers = {}
players = []

class GamePlayServer(asyncio.Protocol):
	timeout_sec = 600.0

	def close_connection(self):
		players.remove(self)
		self.transport.close()

	@asyncio.coroutine
	def handle_received(self, data):
		pass

	def connection_made(self, transport):
		self.transport = transport
		self.h_timeout = asyncio.get_evelop_loop().call_later(self.timeout_sec, self.close_connection)
		players.append(self)

	def data_received(self, data):
		self.h_timeout.cancel()
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.close_connection)
		asyncio.Task(self.handle_received(data))

	def eof_received(self):
		pass

	def connection_lost(self, ex):
		players.remove(self)
		self.h_timeout.cancel()

def main():
	if len(sys.argv) < 2:
		print('Usage: sudo python3 ./GamePlayServer.py develop 00')
		sys.exit()

	phase = sys.argv[1]
	server_id = sys.argv[2]

	# cfg
	with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
		cfg = json.loads(cfg_file.read())

	# log
	log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
	log_handler = logging.handlers.TimedRotatingFileHandler('../log/game_play_server_log_' + server_id + '.csv', when='M', interval=1)
	log_handler.setFormatter(log_formatter)

	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	log.addHandler(log_handler)

	# server
	loop = asyncio.get_event_loop()
	loop.add_signal_handler(signal.SIGINT, loop.stop)
	loop.add_signal_handler(signal.SIGTERM, loop.stop)

	f = loop.create_server(GamePlayServer, port=50002)
	server = loop.run_until_complete(f)

	try:
		loop.run_forever()

	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

if __name__ == '__main__':
	main()

