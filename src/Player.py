
class Player:
    def __init__(self, area_idx):
        self.area_idx = area_idx

    @classmethod
    def run(cls):
        print('player_run')

    def stop(self):
        pass
