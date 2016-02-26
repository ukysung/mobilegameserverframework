
import sys
import logging
import logging.handlers
import json

import g
from bottle import route, request, response, run

def get_log_level(cfg):
    if cfg['log']['level'] == 'debug':
        return logging.DEBUG
    elif cfg['log']['level'] == 'info':
        return logging.INFO
    elif cfg['log']['level'] == 'warn':
        return logging.WARNING
    elif cfg['log']['level'] == 'error':
        return logging.ERROR
    else:
        return logging.DEBUG

def get_log_rotation(cfg):
    if cfg['log']['rotation'] == 'every_minute':
        return 'M'
    elif cfg['log']['rotation'] == 'hourly':
        return 'H'
    elif cfg['log']['rotation'] == 'daily':
        return 'D'
    else:
        return 'M'

if len(sys.argv) < 3:
    print('Usage: sudo python3 ./DataServer.py develop 00')
    sys.exit()

phase = sys.argv[1]
server_seq = sys.argv[2]

# cfg
with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
    cfg = json.loads(cfg_file.read())

log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
log_handler = logging.handlers.TimedRotatingFileHandler(
    '../log/data_server_' + server_seq + '.csv', when=get_log_rotation(cfg), interval=1)
log_handler.setFormatter(log_formatter)

g.LOG = logging.getLogger()
g.LOG.setLevel(get_log_level(cfg))
g.LOG.addHandler(log_handler)

# data_server
server_id = 'server' + server_seq

@route('/')
def index():
    req = request.query.decode()
    res = {'test':req['name']}

    response.content_type = 'application/json'
    return json.dumps(res)

def main():
    run(host='0.0.0.0', port=cfg[server_id]['data_port'])

if __name__ == '__main__':
    main()

