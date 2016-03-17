
import sys
import json
import asyncio

from aiohttp.web import Application, Response, run_app

import g
import config
import logger
import master_data

import boto3

@asyncio.coroutine
def handle_dynamodb(request):
    data = {}
    body = json.dumps(data)

    client = boto3.client('dynamodb', region_name='', endpoint_url='http://127.0.0.1:8000', aws_access_key_id=None, aws_secret_access_key=None)
    print(client.list_tables())

    dynamodb = boto3.resource('dynamodb', region_name='', endpoint_url='http://127.0.0.1:8000', aws_access_key_id=None, aws_secret_access_key=None)
    print(list(dynamodb.tables.all()))

    body = 'OK'
    return Response(body=body.encode('utf-8'))

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

    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./HttpServer.py develop 00')
        sys.exit()

    g.PHASE = sys.argv[1]
    g.SERVER_SEQ = sys.argv[2]

    config.load()
    logger.init(server_type)
    master_data.load()

    # test
    g.MST[1] = 2

    # web_app_server
    app = Application()

    app.router.add_route('GET', '/dynamodb', handle_dynamodb)
    app.router.add_route('GET', '/json', handle_json)
    app.router.add_route('GET', '/{name}', handle_index)
    app.router.add_route('GET', '/', handle_index)

    run_app(app, port=g.CFG[server_type + g.SERVER_SEQ])

if __name__ == '__main__':
    main()

