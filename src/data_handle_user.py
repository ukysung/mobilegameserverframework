
import asyncio
import asyncio.futures

import g
import msg
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

import AESCrypto

from ModelUsers import ModelUsers

def put_user(plat_type, user_id, passwd):
    print(3)
    model_users = ModelUsers()
    model_users.put({
        'plat_type': plat_type,
        'user_id': user_id,
        'passwd': passwd
    })
    print(4)
    print(plat_type)
    print(user_id)
    print(passwd)
    '''
    model_users.put_if_not({
            'platform_type': plat_type,
            'user_id': user_id,
            'passwd': passwd,
            'char_names': []
        },
        'user_id',
        user_id
    )
    '''
    print(5)

@asyncio.coroutine
def handle_sign_up(req_msg_body):
    req = msg_packet_data_pb2.sign_up_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.sign_up_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = ''

    print(1)
    yield from asyncio.futures.wrap_future(g.THREAD_POOL.submit(put_user, req.plat_type, req.user_id, req.passwd))
    print(2)

    ack.err_code = msg_error_pb2.err_none
    ack.auth_token = AESCrypto.auth_token_generator(req.user_id, [])

    return msg.pack(msg_type_data_pb2.t_sign_up_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_sign_up_req] = handle_sign_up

@asyncio.coroutine
def handle_sign_in(req_msg_body):
    req = msg_packet_data_pb2.sign_in_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.sign_in_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = AESCrypto.auth_token_generator(req.user_id, [])

    # do something with db here
    j = yield from asyncio.futures.wrap_future(g.PROC_POOL.submit(b, 1))

    ack.err_code = msg_error_pb2.err_none

    return msg.pack(msg_type_data_pb2.t_sign_in_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_sign_in_req] = handle_sign_in

