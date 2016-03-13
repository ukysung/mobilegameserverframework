
import sys
import multiprocessing
import concurrent.futures
import asyncio
import signal

import config
import logger

import g
from ChannelConnection import handle_internal, handle_outgoing
from ChannelConnection import ChannelConnection
from Channel import Channel

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./ChannelServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]
    server_id = 'server' + server_seq

    config.load(phase)
    logger.init('channel', server_seq)
    #master.load(phase)

    # queues and pool
    g.INCOMING = multiprocessing.Queue()
    g.INTERNAL = multiprocessing.Queue()
    g.OUTGOING = multiprocessing.Queue()
    g.PROCPOOL = concurrent.futures.ProcessPoolExecutor(g.CFG[server_id]['channel_process_pool_size'])

    # channel
    channel = Channel()
    process = multiprocessing.Process(target=channel.run, args=())
    process.start()

    # channel_server
    g.LOOP = asyncio.get_event_loop()
    g.LOOP.add_signal_handler(signal.SIGINT, g.LOOP.stop)
    g.LOOP.add_signal_handler(signal.SIGTERM, g.LOOP.stop)

    task_internal = g.LOOP.create_task(handle_internal())
    task_outgoing = g.LOOP.create_task(handle_outgoing())
    task_server = g.LOOP.create_server(ChannelConnection, port=g.CFG[server_id]['channel_port'])
    channel_server = g.LOOP.run_until_complete(task_server)

    for sock in channel_server.sockets:
        print('channel_server_{} starting.. {}'.format(server_seq, sock.getsockname()))

    try:
        g.LOG.info('channel_server_%s starting.. port %s',
                   server_seq, g.CFG[server_id]['channel_port'])
        g.LOOP.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    finally:
        channel_server.close()

        task_internal.cancel()
        task_outgoing.cancel()

        g.LOOP.run_forever()
        g.LOOP.close()

        g.INCOMING.close()
        g.INTERNAL.close()
        g.OUTGOING.close()
        g.PROCPOOL.shutdown()

        process.join()

if __name__ == '__main__':
    main()

