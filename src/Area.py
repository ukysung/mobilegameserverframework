
# area_types
AREA_LOBBY = 1
AREA_TOWN = 2
AREA_DUNGEON = 3
AREA_ARENA = 4

class Area:
    def __init__(self, area_type):
        self.area_type = area_type
        #self.players = {}
        self.player_conn_ids = []
        self.monsters = []

    def run(self):
        #for player in self.players.values():
            #player.run()

        for monster in self.monsters:
            monster.run()

    def stop(self):
        pass

