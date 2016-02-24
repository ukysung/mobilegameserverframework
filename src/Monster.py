
class Monster:
    def __init__(self, area_id):
        self.area_id = area_id

    @classmethod
    def run(cls):
        print('monster_run')

    def stop(self):
        pass
