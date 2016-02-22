
import time
import asyncio
import struct

import g
import msg_header
from Channel import CHANNEL_ADD_PLAYER, CHANNEL_REMOVE_PLAYER

@asyncio.coroutine
def handle_message_no_1(req_msg_type, req_msg_body):
    print('message_no_1')
    #return (0, req_msg_body)
    return req_msg_body

g.HANDLERS[1] = handle_message_no_1

@asyncio.coroutine
def handle_outgoing():
    while not g.OUTGOING.empty():
        print('handl_n')
        data = yield from g.OUTGOING.get()

    time.sleep(1)
    asyncio.Task(handle_outgoing())

class ChannelConnection(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.timeout_sec = 1800.0
        self.h_timeout = None
        self.msg_buffer = b''

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        g.sess_idx += 1
        if g.sess_idx == 100000:
            g.sess_idx = 1

        g.SESSIONS[g.SESS_IDX] = self
        g.INCOMING.put([1, g.sess_idx])

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        print(data)
        return

        #self.msg_buffer += data
        g.INCOMING.put(data)
        return

        msg_header_offset = 0
        while len(self.msg_buffer) >= (msg_header_offset + msg_header.size):
            msg_body_offset = msg_header_offset + msg_header.size
            (msg_type, msg_size) = struct.unpack(
                'ii', self.msg_buffer[msg_header_offset:msg_body_offset])

            msg_end_offset = msg_header_offset + msg_size
            if len(self.msg_buffer) < msg_end_offset:
                break

            msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
            msg_header_offset = msg_end_offset

            #asyncio.Task(self.handle_received(msg_type, msg_body))

        self.msg_buffer = self.msg_buffer[msg_header_offset:]

        #print(data)
        #for conn in connections:
            #if conn is not self:
                #conn.transport.write(ack)

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()
        #connections.remove(self)

    def connection_timed_out(self):
        self.transport.close()

