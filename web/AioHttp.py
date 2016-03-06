
import asyncio
from aiohttp.web import Application, Response, run_app

@asyncio.coroutine
def handle_index(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'Hello, ' + name

    return Response(body=text.encode('utf-8'))

def main():
    app = Application()

    app.router.add_route('GET', '/', handle_index)
    app.router.add_route('GET', '/{name}', handle_index)

    run_app(app, port=8081)

if __name__ == '__main__':
    main()

