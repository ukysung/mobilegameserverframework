
import json

import g

def load(phase):
    # cfg
    with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
        g.CFG = json.loads(cfg_file.read())

