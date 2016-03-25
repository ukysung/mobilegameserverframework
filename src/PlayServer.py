
import sys
import multiprocessing
import concurrent.futures
import asyncio
import asyncio_redis
import signal

import g
import config
import logger
import master_data

from PlayConnection import handle_internal, handle_outgoing
from PlayConnection import PlayConnection
from PlayLoop import PlayLoop

def shutdown():
    g.SERVER.close()

    g.TASK_INTERNAL.cancel()
    g.TASK_OUTGOING.cancel()

    g.INCOMING.close()
    g.INTERNAL.close()
    g.OUTGOING.close()

    g.REDIS_POOL.close()
    g.THREAD_POOL.shutdown()
    for task in asyncio.Task.all_tasks():
        task.cancel()

    g.PROCESS.join()
    g.LOOP.stop()

def main():
    server_type = 'play'

    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./PlayServer.py develop 00')
        sys.exit()

    g.PHASE = sys.argv[1]
    g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master_data.load()

    # test
    g.MST[1] = 2

    pool_size = g.CFG[server_type + '_thread_pool_size']
    port = g.CFG[server_type + g.SERVER_SEQ]

    # queue
    g.INCOMING = multiprocessing.Queue()
    g.INTERNAL = multiprocessing.Queue()
    g.OUTGOING = multiprocessing.Queue()

    # play
    play_loop = PlayLoop(g.PHASE, g.SERVER_SEQ)
    g.PROCESS = multiprocessing.Process(target=play_loop.run, args=(g.INCOMING, g.INTERNAL, g.OUTGOING))
    g.PROCESS.start()

    # play_server
    g.LOOP = asyncio.get_event_loop()

    # pool
    g.REDIS_POOL = yield from asyncio_redis.Pool.create(host='127.0.0.1', port=6379, poolsize=10)
    g.THREAD_POOL = concurrent.futures.ThreadPoolExecutor(pool_size)

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, shutdown)
        g.LOOP.add_signal_handler(signal.SIGTERM, shutdown)

    except NotImplementedError:
        pass

    g.TASK_INTERNAL = g.LOOP.create_task(handle_internal())
    g.TASK_OUTGOING = g.LOOP.create_task(handle_outgoing())

    coro = g.LOOP.create_server(PlayConnection, port=port)
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

