
import asyncio

clients = []
handlers = {}

class GameProtocol(asyncio.Protocol):
	def connection_made(self, transport):
		self.transport = transport
		self.peername = transport.get_extra_info('peername')
		print(self.peername)
		clients.append(self)

	def data_received(self, data):
		print(data.decode())
		for client in clients:
			if client is not self:
				client.transport.write('{}: {}'.format(self.peername, data.decode()).encode())

	def connection_lost(self, ex):
		print(self.peername)
		clients.remove(self)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	coro = loop.create_server(GameProtocol, port=59999)
	server = loop.run_until_complete(coro)

	for socket in server.sockets:
		print(socket.getsockname())

	try:
		loop.run_forever()

	except KeyboardInterrupt:
		pass

	server.close()
	loop.close()

