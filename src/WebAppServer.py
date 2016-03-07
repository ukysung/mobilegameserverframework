
import sys
import logging
import logging.handlers
import json
import asyncio

from aiohttp.web import Application, Response, run_app
import g

@asyncio.coroutine
def handle_json(request):
    data = {}
    body = json.dumps(data)

    return Response(body=body.encode('utf-8'))

@asyncio.coroutine
def handle_index(request):
    name = request.match_info.get('name', 'Anonymous')
    body = 'Hello, ' + name

    return Response(body=body.encode('utf-8'))

def get_log_level():
    if g.CFG['log']['level'] == 'debug':
        return logging.DEBUG
    elif g.CFG['log']['level'] == 'info':
        return logging.INFO
    elif g.CFG['log']['level'] == 'warn':
        return logging.WARNING
    elif g.CFG['log']['level'] == 'error':
        return logging.ERROR
    else:
        return logging.DEBUG

def get_log_rotation():
    if g.CFG['log']['rotation'] == 'every_minute':
        return 'M'
    elif g.CFG['log']['rotation'] == 'hourly':
        return 'H'
    elif g.CFG['log']['rotation'] == 'daily':
        return 'D'
    else:
        return 'M'

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./DataServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_id = 'server' + sys.argv[2]

    # cfg
    with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
        g.CFG = json.loads(cfg_file.read())

    # log
    log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
    log_handler = logging.handlers.TimedRotatingFileHandler(
        '../log/web_app_server_' + server_seq + '.csv', when=get_log_rotation(), interval=1)
    log_handler.setFormatter(log_formatter)

    g.LOG = logging.getLogger()
    g.LOG.setLevel(get_log_level())
    g.LOG.addHandler(log_handler)

    # mst

    # web_app_server
    app = Application()

    app.router.add_route('GET', '/json', handle_json)
    app.router.add_route('GET', '/{name}', handle_index)
    app.router.add_route('GET', '/', handle_index)

    run_app(app, port=g.CFG[server_id]['http_port'])

if __name__ == '__main__':
    main()

