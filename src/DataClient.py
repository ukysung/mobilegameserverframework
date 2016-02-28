
import sys
import asyncio

@asyncio.coroutine
def DataClient(host, port):
    reader, writer = yield from asyncio.open_connection(host, port)
    writer.write(b'1')

    while True:
        head = yield from reader.read()

    writer.close()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(DataClient(host, port))

if __name__ == '__main__':
    main()

