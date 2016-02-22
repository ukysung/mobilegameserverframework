
class Monster:
    def __init__(self, area_idx):
        self.area_idx = area_idx

    @classmethod
    def run(cls):
        print('monster_run')

    def stop(self):
        pass
