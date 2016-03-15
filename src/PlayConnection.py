
import multiprocessing
import asyncio

import g
import msg
from PlayLoop import PLAYER_CREATE, PLAYER_DELETE

CONNS = {}
INCOMING = multiprocessing.Queue()
INTERNAL = multiprocessing.Queue()
OUTGOING = multiprocessing.Queue()

@asyncio.coroutine
def internal_get():
    return INTERNAL.get()

@asyncio.coroutine
def handle_internal():
    while True:
        if INTERNAL.empty():
            yield from asyncio.sleep(0.001)
            continue

        msg_ = yield from internal_get()
        OUTGOING.put(msg_)

@asyncio.coroutine
def outgoing_get():
    return OUTGOING.get()

@asyncio.coroutine
def handle_outgoing():
    while True:
        if OUTGOING.empty():
            yield from asyncio.sleep(0.001)
            continue

        msg_ = yield from outgoing_get()
        if msg_[0] in CONNS:
            CONNS[msg_[0]].transport.write(b'steve:' + msg_[2])

class PlayConnection(asyncio.Protocol):
    def __init__(self):
        self.loop = g.LOOP
        self.conn_id = 0
        self.transport = None
        self.timeout_sec = g.CFG['server_common']['play_timeout_sec']
        self.h_timeout = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = self.loop.call_later(self.timeout_sec, self.connection_timed_out)

        g.CONN_ID += 1
        if g.CONN_ID == 100000:
            g.CONN_ID = 1

        self.conn_id = g.CONN_ID
        CONNS[self.conn_id] = self

        print('incoming_put')
        INCOMING.put([self.conn_id, PLAYER_CREATE, None])

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = self.loop.call_later(self.timeout_sec, self.connection_timed_out)

        self.msg_buffer += data

        if True:
            print('incoming_put_2')
            INCOMING.put([self.conn_id, 1, self.msg_buffer])
            self.msg_buffer = b''

        else:
            msg_header_offset = 0

            while len(self.msg_buffer) >= (msg_header_offset + msg.HEADER_SIZE):
                msg_body_offset = msg_header_offset + msg.HEADER_SIZE
                (msg_type, msg_size) = msg.unpack_head(
                    self.msg_buffer[msg_header_offset:msg_body_offset])

                msg_end_offset = msg_body_offset + msg_size
                if len(self.msg_buffer) < msg_end_offset:
                    break

                msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
                msg_header_offset = msg_end_offset

                INCOMING.put([self.conn_id, msg_type, msg_body])

            self.msg_buffer = self.msg_buffer[msg_header_offset:]

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()
        conn_id = self.conn_id
        INCOMING.put([conn_id, PLAYER_DELETE, None])
        del CONNS[conn_id]

    def connection_timed_out(self):
        self.transport.close()

