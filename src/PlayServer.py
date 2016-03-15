
import sys
import multiprocessing
import concurrent.futures
import asyncio
import signal

import g
import config
import logger
import master_data

from PlayConnection import INCOMING, INTERNAL, OUTGOING
from PlayConnection import handle_internal, handle_outgoing
from PlayConnection import PlayConnection
from PlayLoop import PlayLoop

def main():
    server_type = 'play'

    if len(sys.argv) > 2:
        g.PHASE = sys.argv[1]
        g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master_data.load()

    # test
    g.MST[1] = 2

    pool_size = g.CFG[server_type + '_proc_pool_size']
    port = g.CFG[server_type + g.SERVER_SEQ]

    # queues and pool
    g.PROC_POOL = concurrent.futures.ProcessPoolExecutor(pool_size)

    # play
    play_loop = PlayLoop(g.PHASE, g.SERVER_SEQ)
    process = multiprocessing.Process(target=play_loop.run, args=(INCOMING, INTERNAL, OUTGOING))
    process.start()

    # play_server
    g.LOOP = asyncio.get_event_loop()

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
        g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    except NotImplementedError:
        pass

    task_internal = g.LOOP.create_task(handle_internal())
    task_outgoing = g.LOOP.create_task(handle_outgoing())

    coro_server = g.LOOP.create_server(PlayConnection, port=port)
    play_server = g.LOOP.run_until_complete(coro_server)

    for sock in play_server.sockets:
        print('{}_server_{} starting.. {}'.format(server_type, g.SERVER_SEQ, sock.getsockname()))

    try:
        g.LOG.info('%s_server_%s starting.. port %s', server_type, g.SERVER_SEQ, port)
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        play_server.close()

        task_internal.cancel()
        task_outgoing.cancel()

        g.LOOP.run_forever()
        g.LOOP.close()

        INCOMING.close()
        INTERNAL.close()
        OUTGOING.close()
        g.PROC_POOL.shutdown()

        process.join()

if __name__ == '__main__':
    main()

