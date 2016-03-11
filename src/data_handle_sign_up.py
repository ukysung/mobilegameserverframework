
import struct
import asyncio

import g
import msg
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

@asyncio.coroutine
def handle_sign_up(req_msg_type, req_msg_body):
    req = msg_packet_data_pb2.sign_up_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.sign_up_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = ''

    # do something with db here

    return msg.pack(msg_type_data_pb2.t_sign_up_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_sign_up_req] = handle_sign_up

