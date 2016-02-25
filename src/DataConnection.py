
import asyncio

import g

from Data_handle_message_no_1 import handle_message_no_1

HANDLERS = {
    1:handle_message_no_1,
}

class DataConnection(asyncio.Protocol):
    def __init__(self):
        g.LOG.info('__init__')
        self.transport = None
        self.timeout_sec = 600.0
        self.h_timeout = None
        self.msg_buffer = b''

    @asyncio.coroutine
    def handle_received(self, req_msg_type, req_msg_body):
        if HANDLERS[req_msg_type] is None:
            return

        ack = yield from HANDLERS[req_msg_type](req_msg_type, req_msg_body)
        self.transport.write(ack)

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        self.msg_buffer += data
        asyncio.Task(self.handle_received(1, self.msg_buffer))
        self.msg_buffer = b''

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()

    def connection_timed_out(self):
        self.transport.close()

