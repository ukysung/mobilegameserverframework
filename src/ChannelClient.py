
import sys
import struct
import asyncio

import msg_header
import msg_type_data_pb2
import msg_struct_pb2
import msg_error_pb2
import msg_packet_data_pb2

HANDLERS = []

def handle_sign_up_req():
    req = msg_packet_data_pb2.sign_up_req()
    req.useremail = 'email@server.com'
    req.passwd = 'password'

    req_str = req.SerializeToString()
    return struct.pack('ii', msg_type_data_pb2.t_sign_up_req, len(req_str)) + req_str
HANDLERS.append(handle_sign_up_req)

def handle_sign_up_ack(msg_body):
    ack = msg_packet_data_pb2.sign_up_ack()
    ack.ParseFromString(msg_body)

    print(ack.authtoken)
HANDLERS.append(handle_sign_up_ack)

@asyncio.coroutine
def ChannelClient(host, port):
    reader, writer = yield from asyncio.open_connection(host, port)

    i = 0
    if len(HANDLERS) == i:
        return
    writer.write(HANDLERS[i]())

    while True:
        msg_head = yield from reader.read(msg_header.size)
        (msg_type, msg_size) = struct.unpack('ii', msg_head)

        msg_body = yield from reader.read(msg_size)

        i += 1
        if len(HANDLERS) == i:
            break
        HANDLERS[i](msg_body)

        i += 1
        if len(HANDLeRS) == i:
            break
        writer.write(HANDLERS[i]())

    writer.close()

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 ./ChannelClient.py 127.0.0.1 22000')
        sys.exit()

    host = sys.argv[1]
    port = sys.argv[2]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(ChannelClient(host, port))

    except KeyboardInterrupt:
        pass

    loop.close()

if __name__ == '__main__':
    main()

