
import logging
import logging.handlers
import json
import multiprocessing
import asyncio
import asyncio.futures
import concurrent.futures
import sys
import signal

import g
from ChannelConnection import INCOMING, INTERNAL, OUTGOING
from ChannelConnection import handle_messageq, handle_outgoing
from ChannelConnection import ChannelConnection
from Channel import Channel

import config
import logger

def init_pool():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./ChannelServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]

    config.load(phase)
    logger.init('channel', server_seq)
    #master.load(phase)

    # channel
    channel = Channel()
    process = multiprocessing.Process(target=channel.run, args=(INCOMING, INTERNAL, OUTGOING))
    process.start()

    # channel_server
    server_id = 'server' + server_seq
    g.P_POOL = concurrent.futures.ProcessPoolExecutor(g.CFG[server_id]['channel_process_pool_size'])

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
        #loop.create_task(handle_messageq())
        #loop.create_task(handle_internal())
        loop.create_task(handle_outgoing())
        loop.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    channel_server.close()

    loop.run_until_complete(channel_server.wait_closed())
    loop.close()

    INCOMING.close()
    INTERNAL.close()
    OUTGOING.close()
    g.P_POOL.shutdown()

    process.join()

if __name__ == '__main__':
    main()

