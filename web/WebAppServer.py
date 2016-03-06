
import sys
import logging
import logging.handlers
import json
import asyncio
import signal

import g
from WebAppConnection import WebAppConnection

def get_log_level():
    if g.CFG['log']['level'] == 'debug':
        return logging.DEBUG
    elif g.CFG['log']['level'] == 'info':
        return logging.INFO
    elif g.CFG['log']['level'] == 'warn':
        return logging.WARNING
    elif g.CFG['log']['level'] == 'error':
        return logging.ERROR
    else:
        return logging.DEBUG

def get_log_rotation():
    if g.CFG['log']['rotation'] == 'every_minute':
        return 'M'
    elif g.CFG['log']['rotation'] == 'hourly':
        return 'H'
    elif g.CFG['log']['rotation'] == 'daily':
        return 'D'
    else:
        return 'M'

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./WebAppServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]

    # cfg
    with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
        g.CFG = json.loads(cfg_file.read())

    # log
    log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
    log_handler = logging.handlers.TimedRotatingFileHandler(
        '../log/web_app_server_' + server_seq + '.csv', when=get_log_rotation(), interval=1)
    log_handler.setFormatter(log_formatter)

    g.LOG = logging.getLogger()
    g.LOG.setLevel(get_log_level())
    g.LOG.addHandler(log_handler)

    # web_app_server
    server_id = 'server' + server_seq
    g.CFG[server_id]['web_app_port'] = 81

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, loop.stop)
    loop.add_signal_handler(signal.SIGTERM, loop.stop)

    coro = loop.create_server(WebAppConnection, port=g.CFG[server_id]['web_app_port'])
    web_app_server = loop.run_until_complete(coro)

    for sock in web_app_server.sockets:
        print('web_app_server_{} starting.. {}'.format(server_seq, sock.getsockname()))

    try:
        g.LOG.info('web_app_server_%s starting.. port %s', server_seq,
                   g.CFG[server_id]['web_app_port'])
        loop.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    web_app_server.close()
    loop.run_until_complete(web_app_server.wait_closed())
    loop.close()

if __name__ == '__main__':
    main()

