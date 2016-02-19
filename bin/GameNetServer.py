from socket import socket, SOL_SOCKET, SO_REUSEADDR
import asyncio
import signal

class Player():
	def __init__(self, net, sock, addr):
		self.net = net
		self.loop = self.net.loop
		self.sock = sock
		self.addr = addr
		self.is_running = True

		asyncio.Task(self.player_main())

	def send(self, data):
		return self.loop.sock_sendall(self.sock, data.encode('utf8'))
	
	@asyncio.coroutine
	def player_main(self):
		try:
			yield from self.player_loop()

		except IOError:
			pass

		finally:
			self.net.remove(self)

	@asyncio.coroutine
	def player_loop(self):
		while self.is_running:
			buf = yield from self.loop.sock_recv(self.sock, 1024)
			if buf == b'':
				break

			self.net.broadcast('%s: %s' % (self.addr, buf.decode('utf8')))

class GameNetServer():
	def __init__(self, loop, port):
		self.loop = loop
		self.net_sock = socket()
		self.net_sock.setblocking(0)
		self.net_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.net_sock.bind(('',port))
		self.net_sock.listen(0)
		self.is_running = True

		self.areas = []
		asyncio.Task(self.run())

	def remove(self, player):
		self.areas.remove(player)
		self.broadcast('Player %s quit!\n' % (player.addr,))

	def broadcast(self, message):
		for player in self.areas:
			player.send(message)

	@asyncio.coroutine
	def run(self):
		while self.is_running:
			player_sock, player_addr = yield from self.loop.sock_accept(self.net_sock)
			player_sock.setblocking(0)
			player = Player(self, player_sock, player_addr)
			self.areas.append(player)
			self.broadcast('Player %s connected!\n' % (player.addr,))

def main():
	loop = asyncio.get_event_loop()
	loop.add_signal_handler(signal.SIGINT, loop.stop)
	loop.add_signal_handler(signal.SIGTERM, loop.stop)

	GameNetServer(loop, 1234)

	try:
		loop.run_forever()

	except KeyboardInterrupt:
		pass

	loop.close()

if __name__ == '__main__':
	main()
