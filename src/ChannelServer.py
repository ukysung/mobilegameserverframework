
import g
import logging, logging.handlers
import json
import multiprocessing
import asyncio
import sys
import signal

from ChannelConnection import handle_outgoing, ChannelConnection
from Channel import Channel

def main():
	if len(sys.argv) < 3:
		print('Usage: sudo python3 ./ChannelServer.py develop 00')
		sys.exit()

	phase = sys.argv[1]
	server_seq = sys.argv[2]

	# cfg
	with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
		cfg = json.loads(cfg_file.read())

	# log
	log_level = None
	log_rotation = None

	if cfg['log']['level'] == 'debug':
		log_level = logging.DEBUG
	elif cfg['log']['level'] == 'info':
		log_level = logging.INFO
	elif cfg['log']['level'] == 'warn':
		log_level = logging.WARNING
	elif cfg['log']['level'] == 'error':
		log_level = logging.ERROR
	else:
		log_level = logging.DEBUG

	if cfg['log']['rotation'] == 'every_minute':
		log_rotation = 'M'
	elif cfg['log']['rotation'] == 'hourly':
		log_rotation = 'H'
	elif cfg['log']['rotation'] == 'daily':
		log_rotation = 'D'
	else:
		log_rotation = 'M'

	log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
	log_handler = logging.handlers.TimedRotatingFileHandler('../log/channel_server_' + server_seq + '.csv', when=log_rotation, interval=1)
	log_handler.setFormatter(log_formatter)

	g.log = logging.getLogger()
	g.log.setLevel(log_level)
	g.log.addHandler(log_handler)

	# multiprocessing
	g.incoming = multiprocessing.Queue()
	g.outgoing = multiprocessing.Queue()

	# channel
	channel = Channel()
	process = multiprocessing.Process(target=channel.run, args=(g.incoming, g.outgoing))
	process.start()

	# channel_server
	server_id = 'server' + server_seq

	loop = asyncio.get_event_loop()
	loop.add_signal_handler(signal.SIGINT, loop.stop)
	loop.add_signal_handler(signal.SIGTERM, loop.stop)

	s = loop.create_server(ChannelConnection, port=cfg[server_id]['channel_port'])
	channel_server = loop.run_until_complete(s)

	for s in channel_server.sockets:
		print('channel_server_{} starting.. {}'.format(server_seq, s.getsockname()))

	try:
		g.log.info('channel_server_%s starting.. port %s', server_seq, cfg[server_id]['channel_port'])
		loop.create_task(handle_outgoing())
		loop.run_forever()

	except KeyboardInterrupt:
		g.log.info('keyboard interrupt..')
		pass

	channel_server.close()

	loop.run_until_complete(channel_server.wait_closed())
	loop.close()

	g.incoming.close()
	g.outgoing.close()
	#process.terminate()
	process.join()

if __name__ == '__main__':
	main()

