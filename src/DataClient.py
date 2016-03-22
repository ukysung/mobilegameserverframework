
import sys
import time
import asyncio

import msg
import msg_type_data_pb2
import msg_enum_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

TIME = str(int(time.time()))

VARS = {
    'host': 'localhost',
    'port': 21000,
    'user_id': 'u' + TIME,
    'passwd': 'p' + TIME,
    'auth_token': '',
    'char_mid': 1,
    'char_name': 'c' + TIME,
    'dungeon_mid': 1,
}

HANDLERS = []

def handle_sign_up_req():
    print(sys._getframe().f_code.co_name)

    req = msg_packet_data_pb2.sign_up_req()
    req.plat_type = msg_enum_pb2.plat_none
    req.user_id = VARS['user_id']
    req.passwd = VARS['passwd']

    return msg.pack(msg_type_data_pb2.t_sign_up_req, req)
HANDLERS.append(handle_sign_up_req)

def handle_sign_up_ack(msg_body):
    print(sys._getframe().f_code.co_name)

    ack = msg_packet_data_pb2.sign_up_ack()
    ack.ParseFromString(msg_body)

    print('auth_token : ' + ack.auth_token)
    VARS['auth_token'] = ack.auth_token
HANDLERS.append(handle_sign_up_ack)

def handle_sign_in_req():
    print(sys._getframe().f_code.co_name)

    req = msg_packet_data_pb2.sign_in_req()
    req.plat_type = msg_enum_pb2.plat_none
    req.user_id = VARS['user_id']
    req.passwd = VARS['passwd']

    return msg.pack(msg_type_data_pb2.t_sign_in_req, req)
HANDLERS.append(handle_sign_in_req)

def handle_sign_in_ack(msg_body):
    print(sys._getframe().f_code.co_name)

    ack = msg_packet_data_pb2.sign_in_ack()
    ack.ParseFromString(msg_body)

    print('auth_token : ' + ack.auth_token)
    VARS['auth_token'] = ack.auth_token
HANDLERS.append(handle_sign_in_ack)

def handle_create_character_req():
    print(sys._getframe().f_code.co_name)

    req = msg_packet_data_pb2.create_character_req()
    req.auth_token = VARS['auth_token']
    req.char_mid = VARS['char_mid']
    req.char_name = VARS['char_name']

    return msg.pack(msg_type_data_pb2.t_create_character_req, req)
HANDLERS.append(handle_create_character_req)

def handle_create_character_ack(msg_body):
    print(sys._getframe().f_code.co_name)

    ack = msg_packet_data_pb2.create_character_ack()
    ack.ParseFromString(msg_body)

    print('auth_token : ' + ack.auth_token)
    VARS['auth_token'] = ack.auth_token
HANDLERS.append(handle_create_character_ack)


@asyncio.coroutine
def data_client(host, port):
    reader, writer = yield from asyncio.open_connection(host, port)

    i = 0
    if len(HANDLERS) == i:
        return
    writer.write(HANDLERS[i]())
    print()

    while True:
        msg_head = yield from reader.read(msg.HEADER_SIZE)
        (msg_type, msg_size) = msg.unpack_head(msg_head)

        msg_body = yield from reader.read(msg_size)

        i += 1
        if len(HANDLERS) == i:
            break
        HANDLERS[i](msg_body)
        print()

        i += 1
        if len(HANDLERS) == i:
            break
        writer.write(HANDLERS[i]())
        print()

    writer.close()
    print('\nOKAY\n')

def main():
    if len(sys.argv) < 7:
        print('\nUsage: python3 ./DataClient.py host port user_id passwd \
              char_mid char_name dungeon_mid\n')

        for key in VARS:
            print(key + ' : ' + str(VARS[key]))
        print()

    else:
        VARS['host'] = sys.argv[1]
        VARS['port'] = sys.argv[2]
        VARS['user_id'] = sys.argv[3]
        VARS['passwd'] = sys.argv[4]
        VARS['char_mid'] = int(sys.argv[5])
        VARS['char_name'] = sys.argv[6]
        VARS['dungeon_mid'] = sys.argv[7]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(data_client(VARS['host'], VARS['port']))

    except KeyboardInterrupt:
        pass

    loop.close()

if __name__ == '__main__':
    main()

