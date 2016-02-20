
import g
import sys
import logging, logging.handlers
import json
import asyncio
import signal

from DataConnection import DataConnection

def main():
	if len(sys.argv) < 3:
		print('Usage: sudo python3 ./DataServer.py develop 00')
		sys.exit()

	phase = sys.argv[1]
	server_seq = sys.argv[2]

	# cfg
	with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
		g.cfg = json.loads(cfg_file.read())

	# log
	log_level = None
	log_rotation = None

	if g.cfg['log']['level'] == 'debug':
		log_level = logging.DEBUG
	elif g.cfg['log']['level'] == 'info':
		log_level = logging.INFO
	elif g.cfg['log']['level'] == 'warn':
		log_level = logging.WARNING
	elif g.cfg['log']['level'] == 'error':
		log_level = logging.ERROR
	else:
		log_level = logging.DEBUG

	if g.cfg['log']['rotation'] == 'every_minute':
		log_rotation = 'M'
	elif g.cfg['log']['rotation'] == 'hourly':
		log_rotation = 'H'
	elif g.cfg['log']['rotation'] == 'daily':
		log_rotation = 'D'
	else:
		log_rotation = 'M'

	log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
	log_handler = logging.handlers.TimedRotatingFileHandler('../log/data_server_' + server_seq + '.csv', when=log_rotation, interval=1)
	log_handler.setFormatter(log_formatter)

	g.log = logging.getLogger()
	g.log.setLevel(log_level)
	g.log.addHandler(log_handler)

	# data_server
	server_id = 'server' + server_seq

	loop = asyncio.get_event_loop()
	loop.add_signal_handler(signal.SIGINT, loop.stop)
	loop.add_signal_handler(signal.SIGTERM, loop.stop)

	f = loop.create_server(DataConnection, port=g.cfg[server_id]['data_port'])
	data_server = loop.run_until_complete(f)

	for s in data_server.sockets:
		print('data_server_{} starting.. {}'.format(server_seq, s.getsockname()))

	try:
		g.log.info('data_server_%s starting.. port %s', server_seq, g.cfg[server_id]['data_port'])
		loop.run_forever()

	except KeyboardInterrupt:
		g.log.info('keyboard interrupt..')
		pass

	data_server.close()
	loop.run_until_complete(data_server.wait_closed())
	loop.close()

if __name__ == '__main__':
	main()

