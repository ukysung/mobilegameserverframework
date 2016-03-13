
import sys
import asyncio
import asyncio.futures
import concurrent.futures
import signal

import config
import logger

import g
from DataConnection import DataConnection

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./DataServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]
    server_id = 'server' + server_seq

    config.load(phase)
    logger.init('data', server_seq)
    #master.load(phase)

    # pool
    g.PROCPOOL = concurrent.futures.ProcessPoolExecutor(g.CFG[server_id]['data_process_pool_size'])

    # data_server
    g.LOOP = asyncio.get_event_loop()
    g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
    g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    coro = g.LOOP.create_server(DataConnection, port=g.CFG[server_id]['data_port'])
    data_server = g.LOOP.run_until_complete(coro)

    for sock in data_server.sockets:
        print('data_server_{} starting.. {}'.format(server_seq, sock.getsockname()))

    try:
        g.LOG.info('data_server_%s starting.. port %s', server_seq, g.CFG[server_id]['data_port'])
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        data_server.close()
        g.LOOP.close()

        g.PROCPOOL.shutdown()

if __name__ == '__main__':
    main()

