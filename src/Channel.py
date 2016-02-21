
from Area import area_lobby, area_town, area_dungeon, area_arena, Area
from Player import Player
import signal
import time

channel_add_player = 1
channel_remove_player = 2

class Channel:
	def __init__(self):
		signal.signal(signal.SIGINT, self.stop)
		signal.signal(signal.SIGTERM, self.stop)

		self.mst = {}
		self.is_running = True
		self.process_incoming_max = 100
		self.area_idx = 0
		self.areas = {}
		self.areas[self.area_idx] = Area(area_lobby)

	def run(self, incoming, outgoing):
		print('channel_run')

		process_incoming = False
		while self.is_running:
			if process_incoming:
				#print('incoming')
				i = 0
				while i < self.process_incoming_max and not incoming.empty():
					i += 1

					(msg_type, msg_body) = incoming.get()
					if msg_type == channel_add_player:
						self.areas[0][msg_body] = Player(msg_body)

				print('process_incoming')
				time.sleep(1)
				process_incoming = False

			else:
				for area in self.areas:
					area.run()
				print('loop')
				time.sleep(1)
				process_incoming = True

	def stop(self, signal_num, frame_obj):
		print('stop_called')
		self.is_running = False

