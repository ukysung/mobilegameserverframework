
import sys
import asyncio

import msg
import msg_type_data_pb2
import msg_enum_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

HANDLERS = []

def handle_sign_up_req():
    req = msg_packet_data_pb2.sign_up_req()
    req.plat_type = msg_enum_pb2.plat_none
    req.userid = 'email@server.com'
    req.passwd = 'my_passwd'

    return msg.pack(msg_type_data_pb2.t_sign_up_req, req)
HANDLERS.append(handle_sign_up_req)

def handle_sign_up_ack(msg_body):
    print(1)
    ack = msg_packet_data_pb2.sign_up_ack()
    print(2)
    ack.ParseFromString(msg_body)
    print(3)

    print('auth_token:' + ack.auth_token)
HANDLERS.append(handle_sign_up_ack)

@asyncio.coroutine
def data_client(host, port):
    reader, writer = yield from asyncio.open_connection(host, port)

    i = 0
    if len(HANDLERS) == i:
        return
    writer.write(HANDLERS[i]())

    while True:
        msg_head = yield from reader.read(msg.HEADER_SIZE)
        (msg_type, msg_size) = msg.unpack_head(msg_head)

        msg_body = yield from reader.read(msg_size)

        i += 1
        if len(HANDLERS) == i:
            break
        HANDLERS[i](msg_body)

        i += 1
        if len(HANDLERS) == i:
            break
        writer.write(HANDLERS[i]())

    writer.close()

def main():
    host = 'localhost'
    port = 21000

    if len(sys.argv) > 2:
        host = sys.argv[1]
        port = int(sys.argv[2])

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(data_client(host, port))

    except KeyboardInterrupt:
        pass

    loop.close()

if __name__ == '__main__':
    main()

