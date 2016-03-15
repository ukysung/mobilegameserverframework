
from os import listdir
from os.path import isfile, join

import msgpack
import g

def load():
    path = '../mst/' + g.PHASE + '_msgpacked'
    files = [f for f in listdir(path) if isfile(join(path, f))]

    for file_ in files:
        name = file_.replace('.msgpacked', '')

        with open('../mst/' + g.PHASE + '_msgpacked/' + file_, 'rb') as mst_file:
            g.MST[name] = msgpack.unpackb(mst_file.read())

