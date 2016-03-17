
import g
from GameMachine import GameMachine

class Area:
    def __init__(self, area_type):
        g.LOG.info('area__init__')
        self.area_type = area_type
        self.game_machine = GameMachine()
        self.player_conn_ids = []
        self.monsters = []

    def run(self, delta_time):
        for monster in self.monsters:
            monster.run(delta_time)

        self.game_machine.run(delta_time)

