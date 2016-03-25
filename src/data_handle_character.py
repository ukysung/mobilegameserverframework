
import asyncio
from asyncio.futures import wrap_future

import g
import msg
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

import AESCrypto

from ModelCharacters import ModelCharacters
import data_handle_user as user

def test1():
    print('test1')

def put_character(req, user_id):
    print(3)
    model_characters = ModelCharacters()
    model_characters.put({
        'char_name': req.char_name,
        'user_id': user_id,
        'char_mid': req.char_mid
    })
    print(4)
    print(req.char_name)
    print(req.char_mid)
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
    char_names = user.add_character(user_id, req.char_name)
    return char_names

@asyncio.coroutine
def handle_create_character(req_msg_body):
    req = msg_packet_data_pb2.create_character_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.create_character_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = ''

    user_id = AESCrypto.get_user_id(req.auth_token)

    print(1)
    char_names = yield from wrap_future(g.THREAD_POOL.submit(put_character, req, user_id))
    print(2)

    ack.err_code = msg_error_pb2.err_none
    ack.auth_token = AESCrypto.generate_auth_token(user_id, char_names)

    return msg.pack(msg_type_data_pb2.t_sign_up_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_create_character_req] = handle_create_character

@asyncio.coroutine
def handle_get_char_list(req_msg_body):
    req = msg_packet_data_pb2.get_char_list_req()
    req.ParseFromString(req_msg_body)

    ack = msg_packet_data_pb2.get_char_list_ack()
    ack.err_code = msg_error_pb2.err_server_unknown
    ack.auth_token = ''

    # do something with db here
    j = yield from asyncio.futures.wrap_future(g.THREAD_POOL.submit(b, 1))

    ack.err_code = msg_error_pb2.err_none

    return msg.pack(msg_type_data_pb2.t_sign_in_ack, ack)
g.DATA_HANDLERS[msg_type_data_pb2.t_get_char_list_req] = handle_get_char_list

