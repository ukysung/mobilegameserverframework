
import asyncio
from aiohttp.web import Application, Response, run_app

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
    app = Application()

    app.router.add_route('GET', '/json', handle_json)
    app.router.add_route('GET', '/{name}', handle_index)
    app.router.add_route('GET', '/', handle_index)

    run_app(app, port=8081)

if __name__ == '__main__':
    main()

