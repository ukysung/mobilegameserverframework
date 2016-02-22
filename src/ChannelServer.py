
import logging
import logging.handlers
import json
import multiprocessing
import asyncio
import sys
import signal

import g
from ChannelConnection import handle_outgoing, ChannelConnection
from Channel import Channel

def get_log_level(cfg):
    if cfg['log']['level'] == 'debug':
        return logging.DEBUG
    elif cfg['log']['level'] == 'info':
        return logging.INFO
    elif cfg['log']['level'] == 'warn':
        return logging.WARNING
    elif cfg['log']['level'] == 'error':
        return logging.ERROR
    else:
        return logging.DEBUG

def get_log_rotation(cfg):
    if cfg['log']['rotation'] == 'every_minute':
        return 'M'
    elif cfg['log']['rotation'] == 'hourly':
        return 'H'
    elif cfg['log']['rotation'] == 'daily':
        return 'D'
    else:
        return 'M'

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./ChannelServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]

    # cfg
    with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
        g.CFG = json.loads(cfg_file.read())

    log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
    log_handler = logging.handlers.TimedRotatingFileHandler(
        '../log/channel_server_' + server_seq + '.csv', when=get_log_rotation(g.CFG), interval=1)
    log_handler.setFormatter(log_formatter)

    g.LOG = logging.getLogger()
    g.LOG.setLevel(get_log_level(g.CFG))
    g.LOG.addHandler(log_handler)

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

    coro = loop.create_server(ChannelConnection, port=g.CFG[server_id]['channel_port'])
    channel_server = loop.run_until_complete(coro)

    for sock in channel_server.sockets:
        print('channel_server_{} starting.. {}'.format(server_seq, sock.getsockname()))

    try:
        g.LOG.info('channel_server_%s starting.. port %s',
                   server_seq, g.CFG[server_id]['channel_port'])
        loop.create_task(handle_outgoing())
        loop.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    channel_server.close()

    loop.run_until_complete(channel_server.wait_closed())
    loop.close()

    g.incoming.close()
    g.outgoing.close()
    process.join()

if __name__ == '__main__':
    main()

