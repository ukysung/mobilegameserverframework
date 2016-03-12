
import sys
import json
import asyncio

from aiohttp.web import Application, Response, run_app

import g
import config
import logger

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

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./DataServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]
    server_id = 'server' + server_seq

    config.load(phase)
    logger.init('web_app', server_seq)
    #master.load(phase)

    # web_app_server
    app = Application()

    app.router.add_route('GET', '/json', handle_json)
    app.router.add_route('GET', '/{name}', handle_index)
    app.router.add_route('GET', '/', handle_index)

    run_app(app, port=g.CFG[server_id]['http_port'])

if __name__ == '__main__':
    main()

