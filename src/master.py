
import json

from os import listdir
from os.path import isfile, join

import g

def load():
    path = '../mst/' + g.PHASE + '_json'
    files = [f for f in listdir(path) if isfile(join(path, f))]

    for f in files:
        name = f.replace('.json', '')
        with open('../mst/' + g.PHASE + '_json/' + f, encoding='utf-8') as cfg_file:
            g.MST[name] = json.loads(cfg_file.read())

