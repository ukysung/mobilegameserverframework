
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
    if len(sys.argv) > 2:
        g.PHASE = sys.argv[1]
        g.SERVER_SEQ = sys.argv[2]
        g.SERVER_ID = 'server' + g.SERVER_SEQ

    config.load()
    logger.init('data')
    #master.load()
    g.MST[1] = 2

    pool_size = g.CFG[g.SERVER_ID]['data_process_pool_size']
    port = g.CFG[g.SERVER_ID]['data_port']

    # pool
    g.PROC_POOL = concurrent.futures.ProcessPoolExecutor(pool_size)

    # data_server
    g.LOOP = asyncio.get_event_loop()

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
        g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    except:
        pass

    coro_server = g.LOOP.create_server(DataConnection, port=port)
    data_server = g.LOOP.run_until_complete(coro_server)

    for sock in data_server.sockets:
        print('data_server_{} starting.. {}'.format(g.SERVER_SEQ, sock.getsockname()))

    try:
        g.LOG.info('data_server_%s starting.. port %s', g.SERVER_SEQ, port)
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        data_server.close()
        g.LOOP.close()

        g.PROC_POOL.shutdown()

if __name__ == '__main__':
    main()

