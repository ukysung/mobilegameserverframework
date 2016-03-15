
import sys
import json
import asyncio

from aiohttp.web import Application, Response, run_app

import config
import logger
import master

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

def main():
    server_type = 'http'

    if len(sys.argv) > 3:
        g.PHASE = sys.argv[1]
        g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master.load()

    # web_app_server
    app = Application()

    app.router.add_route('GET', '/json', handle_json)
    app.router.add_route('GET', '/{name}', handle_index)
    app.router.add_route('GET', '/', handle_index)

    run_app(app, port=g.CFG[server_type + g.SERVER_SEQ])

if __name__ == '__main__':
    main()

