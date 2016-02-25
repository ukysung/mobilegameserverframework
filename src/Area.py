
from GameMachine import GameMachine

# area_types
AREA_LOBBY = 1
AREA_TOWN = 2
AREA_DUNGEON = 3
AREA_ARENA = 4

class Area:
    def __init__(self, area_type):
        self.area_type = area_type
        self.game_machine = GameMachine()
        self.player_conn_ids = []
        self.monsters = []

    def run(self, delta_time):
        for monster in self.monsters:
            monster.run(delta_time)

        self.game_machine.run(delta_time)

