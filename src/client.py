
import asyncio

'''
struct
{
	int32_t msg_type; // 4 bytes
	int32_t msg_size; // 4 bytes
}
// totally 8 bytes
'''
msg_head_size = 8

@asyncio.coroutine
def client():
	(reader, writer) = yield from asyncio.open_connection('localhost', 59999)
	writer.write(b'1234567890)

	while True:
		#req_msg_type = 1
		#req_msg_body = '11'
		#req_head = struct.pack('ii', req_msg_type, len(req_msg_body))

		ack_head = yield from reader.read(msg_head_size)

		ack = yield from reader.read(ack_
		if len(body) = 0:
			break

	writer.close()
		
def main():
	loop = asyncio.get_event_loop()

	try:
		loop.run_until_complete(client())

	except KeyboardInterrupt:
		pass

	loop.close()

if __name__ == '__main__':
	main()
