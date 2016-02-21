
# area_types
area_lobby = 1
area_town = 2
area_dungeon = 3
area_arena = 4

class Area:
	def __init__(self, area_type):
		self.area_type = area_type
		self.players = {}
		self.monsters = []

	def run(self):
		for player in self.players:
			player.run()

		for monster in self.monsters:
			monster.run()

