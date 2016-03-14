
import sys
import multiprocessing
import concurrent.futures
import asyncio
import signal

import config
import logger

import g
from ChannelConnection import INCOMING, INTERNAL, OUTGOING
from ChannelConnection import handle_internal, handle_outgoing
from ChannelConnection import ChannelConnection
from Channel import Channel

def main():
    if len(sys.argv) > 2:
        g.PHASE = sys.argv[1]
        g.SERVER_SEQ = sys.argv[2]
        g.SERVER_ID = 'server' + g.SERVER_SEQ

    config.load()
    logger.init('channel')
    #master.load()
    g.MST[1] = 2

    pool_size = g.CFG[g.SERVER_ID]['channel_process_pool_size']
    timeout_sec = g.CFG[g.SERVER_ID]['channel_timeout_sec']
    port = g.CFG[g.SERVER_ID]['channel_port']

    # queues and pool
    g.PROC_POOL = concurrent.futures.ProcessPoolExecutor(pool_size)

    # channel
    channel = Channel(g.PHASE, g.SERVER_SEQ)
    process = multiprocessing.Process(target=channel.run, args=(INCOMING, INTERNAL, OUTGOING))
    process.start()

    # channel_server
    g.LOOP = asyncio.get_event_loop()

    try:
        g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
        g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    except:
        pass

    task_internal = g.LOOP.create_task(handle_internal())
    task_outgoing = g.LOOP.create_task(handle_outgoing())
    coro_server = g.LOOP.create_server(ChannelConnection, port=port)
    channel_server = g.LOOP.run_until_complete(coro_server)

    for sock in channel_server.sockets:
        print('channel_server_{} starting.. {}'.format(g.SERVER_SEQ, sock.getsockname()))

    try:
        g.LOG.info('channel_server_%s starting.. port %s', g.SERVER_SEQ, port)
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        channel_server.close()

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

