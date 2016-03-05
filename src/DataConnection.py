
import struct
import asyncio

import g
import msg_header
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

from data_handle_sign_up import handle_sign_up
#from data_handle_sign_in import handle_sign_in

HANDLERS = {
    msg_type_data_pb2.t_sign_up_req:handle_sign_up,
    #msg_type_data_pb2.t_sign_in_req:handle_sign_in,
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

        if False:
            asyncio.Task(self.handle_received(1, self.msg_buffer))
            self.msg_buffer = b''

        else:
            msg_header_offset = 0

            while len(self.msg_buffer) >= (msg_header_offset + msg_header.size):
                msg_body_offset = msg_header_offset + msg_header.size
                (msg_type, msg_size) = struct.unpack(
                    'ii', self.msg_buffer[msg_header_offset:msg_body_offset])

                msg_end_offset = msg_body_offset + msg_size
                if len(self.msg_buffer) < msg_end_offset:
                    break

                msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
                msg_header_offset = msg_end_offset

                asyncio.Task(self.handle_received(msg_type, msg_body))

            self.msg_buffer = self.msg_buffer[msg_header_offset:]

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()

    def connection_timed_out(self):
        self.transport.close()

