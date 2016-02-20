
import time

class GameChannel():
	def __init__(self):
		self.is_running = True
		pass

	def run(self):
		while self.is_running:
			print('game_channel')
			time.sleep(1.0)

	def stop(self):
		lock = multiprocessing.Lock()
		lock.acquire()
		self.is_running = False
		lock.release()


