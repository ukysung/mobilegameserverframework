
import asyncio
from asyncio.futures import wrap_future

import g
import msg
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

import AESCrypto

from ModelUsers import ModelUsers
import data_handle_character as character

def test2():
    print('test2')

def put_user(req):
    character.test1()
    print(3)
    model_users = ModelUsers()
    model_users.put({
        'plat_type': req.plat_type,
        'user_id': req.user_id,
        'passwd': req.passwd,
        'char_names': []
    })
    print(4)
    print(req.plat_type)
    print(req.user_id)
    print(req.passwd)
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

def add_character(user_id, char_name):
    model_users = ModelUsers()
    model_users.append(
        {'user_id': user_id},
        'char_names',
        char_name
    )

@asyncio.coroutine
def handle_sign_up(req_msg_body):
    req = msg_packet_data_pb2.sign_up_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.sign_up_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = ''

    print(1)
    yield from wrap_future(g.THREAD_POOL.submit(put_user, req))
    print(2)

    ack.err_code = msg_error_pb2.err_none
    ack.auth_token = AESCrypto.generate_auth_token(req.user_id, [])

    return msg.pack(msg_type_data_pb2.t_sign_up_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_sign_up_req] = handle_sign_up

@asyncio.coroutine
def handle_sign_in(req_msg_body):
    req = msg_packet_data_pb2.sign_in_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.sign_in_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = AESCrypto.generate_auth_token(req.user_id, [])

    # do something with db here
    #j = yield from asyncio.futures.wrap_future(g.THREAD_POOL.submit(b, 1))

    ack.err_code = msg_error_pb2.err_none

    return msg.pack(msg_type_data_pb2.t_sign_in_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_sign_in_req] = handle_sign_in

