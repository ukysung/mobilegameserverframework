
import sys
import asyncio

import msg
import msg_type_play_pb2
import msg_enum_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_play_pb2

VARS = {
    'host': 'localhost',
    'port': 22000,
    'auth_token': '',
    'char_name': 'chr_01',
    'dungeon_mid': 1,
}

HANDLERS = []

def handle_enter_town_req():
    print(sys._getframe().f_code.co_name)

    req = msg_packet_play_pb2.enter_town_req()

    return msg.pack(msg_type_play_pb2.t_enter_town_req, req)
HANDLERS.append(handle_enter_town_req)

def handle_enter_town_ack(msg_body):
    print(sys._getframe().f_code.co_name)

    ack = msg_packet_play_pb2.enter_town_ack()
    ack.ParseFromString(msg_body)

    print(ack.err_code)
HANDLERS.append(handle_enter_town_ack)

@asyncio.coroutine
def play_client(host, port):
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
    if len(sys.argv) < 5:
        print('\nUsage: python3 ./PlayClient.py host port auth_token char_name dungeon_mid\n')

        for key in VARS:
            print(key + ' : ' + str(VARS[key]))
        print()

    else:
        VARS['host'] = sys.argv[1]
        VARS['port'] = sys.argv[2]
        VARS['auth_token'] = sys.argv[3]
        VARS['char_name'] = sys.argv[4]
        VARS['dungeon_mid'] = sys.argv[5]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(play_client(host, port))

    except KeyboardInterrupt:
        pass

    loop.close()

if __name__ == '__main__':
    main()

