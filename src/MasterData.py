
import json

from os import listdir
from os.path import isfile, join

import g

class MasterData:
    def __init__(self):
        self.mst = {}

    def load(self):
        path = '../mst/' + g.PHASE + '_json'
        files = [f for f in listdir(path) if isfile(join(path, f))]

        for file_ in files:
            name = file_.replace('.json', '')

            with open('../mst/' + g.PHASE + '_json/' + file_, encoding='utf-8') as cfg_file:
                self.mst[name] = json.loads(cfg_file.read())

    def get(self, table, mid):
        return self.mst[table][str(mid)]

