
class Player:
	def __init__(self, area_idx):
		self.area_idx = area_idx

		self.sess.set_player(self)

	def run(self):
		print('player_run')

