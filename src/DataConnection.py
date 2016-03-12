
import asyncio

import g
import msg
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

from data_handle_sign_up import handle_sign_up
#from data_handle_sign_in import handle_sign_in

class DataConnection(asyncio.Protocol):
    def __init__(self):
        g.LOG.info('__init__')
        self.transport = None
        self.timeout_sec = 600.0
        self.h_timeout = None
        self.msg_buffer = b''

    @asyncio.coroutine
    def handle_received(self, req_msg_type, req_msg_body):
        if req_msg_type not in g.DATA_HANDLERS:
            g.LOG.error('handler for %s is not imported to DataConnection', req_msg_type)
            return

        ack = yield from g.DATA_HANDLERS[req_msg_type](req_msg_type, req_msg_body)
        self.transport.write(ack)

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = g.LOOP.call_later(self.timeout_sec, self.connection_timed_out)

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = g.LOOP.call_later(self.timeout_sec, self.connection_timed_out)

        self.msg_buffer += data

        if False:
            g.LOOP.create_task(self.handle_received(1, self.msg_buffer))
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

                g.LOOP.create_task(self.handle_received(msg_type, msg_body))

            self.msg_buffer = self.msg_buffer[msg_header_offset:]

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()

    def connection_timed_out(self):
        self.transport.close()

