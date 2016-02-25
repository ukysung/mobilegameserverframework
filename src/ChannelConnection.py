
import time
import multiprocessing
import asyncio

import g
from Channel import CHANNEL_ADD_PLAYER, CHANNEL_REMOVE_PLAYER

CONNS = {}

INCOMING = multiprocessing.Queue()
OUTGOING = multiprocessing.Queue()

@asyncio.coroutine
def outgoing_get(outgoing):
    msgs = []

    i = 0
    while i < 1000 and not outgoing.empty():
        i += 1
        msgs.append(outgoing.get())

    return msgs

@asyncio.coroutine
def handle_outgoing(outgoing):
    msgs = yield from outgoing_get(outgoing)
    for msg in msgs:
        if CONNS[msg[0]] is not None:
            CONNS[msg[0]].transport.write(b'steve:' + msg[2])

    time.sleep(3.0 / 1000.0)
    asyncio.Task(handle_outgoing(outgoing))

class ChannelConnection(asyncio.Protocol):
    def __init__(self):
        self.conn_id = 0
        self.transport = None
        self.timeout_sec = 1800.0
        self.h_timeout = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        g.CONN_ID += 1
        if g.CONN_ID == 100000:
            g.CONN_ID = 1

        self.conn_id = g.CONN_ID
        CONNS[self.conn_id] = self

        print('incoming_put')
        INCOMING.put([self.conn_id, CHANNEL_ADD_PLAYER, None])

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        self.msg_buffer += data
        print('incoming_put_2')
        INCOMING.put([self.conn_id, 1, self.msg_buffer])
        self.msg_buffer = b''

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()
        INCOMING.put([self.conn_id, CHANNEL_REMOVE_PLAYER, None])

    def connection_timed_out(self):
        self.transport.close()

