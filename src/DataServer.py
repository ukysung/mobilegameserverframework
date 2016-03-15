
import sys
import asyncio
import asyncio.futures
import concurrent.futures
import signal

import config
import logger
import master

import g
from DataConnection import DataConnection

def main():
    server_type = 'data'

    if len(sys.argv) > 2:
        g.PHASE = sys.argv[1]
        g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master.load()
    g.MST[1] = 2

    pool_size = g.CFG['server_common'][server_type + '_proc_pool_size']
    port = g.CFG[server_type + g.SERVER_SEQ]

    # pool
    g.PROC_POOL = concurrent.futures.ProcessPoolExecutor(pool_size)

    # data_server
    g.LOOP = asyncio.get_event_loop()

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
        g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    except NotImplementedError:
        pass

    coro_server = g.LOOP.create_server(DataConnection, port=port)
    data_server = g.LOOP.run_until_complete(coro_server)

    for sock in data_server.sockets:
        print('{}_server_{} starting.. {}'.format(server_type, g.SERVER_SEQ, sock.getsockname()))

    try:
        g.LOG.info('%s_server_%s starting.. port %s', server_type, g.SERVER_SEQ, port)
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        data_server.close()
        g.LOOP.close()

        g.PROC_POOL.shutdown()

if __name__ == '__main__':
    main()

