
import sys
import asyncio
import asyncio.futures
import concurrent.futures
import signal

import g
import config
import logger
import master_data

from DataConnection import DataConnection

def shutdown():
    g.SERVER.close()

    g.THREAD_POOL.shutdown()
    for task in asyncio.Task.all_tasks():
        task.cancel()

    g.LOOP.stop()

def main():
    server_type = 'data'

    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./DataServer.py develop 00')
        sys.exit()

    g.PHASE = sys.argv[1]
    g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master_data.load()

    # test
    g.MST[1] = 2

    pool_size = g.CFG[server_type + '_proc_pool_size']
    port = g.CFG[server_type + g.SERVER_SEQ]

    # pool
    g.THREAD_POOL = concurrent.futures.ThreadPoolExecutor(pool_size)

    # data_server
    g.LOOP = asyncio.get_event_loop()

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, shutdown)
        g.LOOP.add_signal_handler(signal.SIGTERM, shutdown)

    except NotImplementedError:
        pass

    coro = g.LOOP.create_server(DataConnection, port=port)
    g.SERVER = g.LOOP.run_until_complete(coro)

    for sock in g.SERVER.sockets:
        print('{}_server_{} starting.. {}'.format(server_type, g.SERVER_SEQ, sock.getsockname()))

    try:
        g.LOG.info('%s_server_%s starting.. port %s', server_type, g.SERVER_SEQ, port)
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        shutdown()

if __name__ == '__main__':
    main()

