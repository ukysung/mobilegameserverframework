
import json

import g

def load():
    # cfg
    with open('../cfg/' + g.PHASE + '.json', encoding='utf-8') as cfg_file:
        g.CFG = json.loads(cfg_file.read())

