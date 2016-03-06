
import json
import time
import asyncio

import g

WEEK_DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

class WebAppConnection(asyncio.Protocol):
    def __init__(self):
        g.LOG.info('__init__')
        self.transport = None
        self.timeout_sec = 3.0
        self.h_timeout = None
        self.msg_buffer = b''

    @asyncio.coroutine
    def handle_received(self, http_req):
        data = {}
        json_str = json.dumps(data)

        date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        last_modified = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())

        http_res = ('HTTP/1.1 200 OK\r\nServer: WebAppServer\r\nDate: ' + date +
                    '\r\nContent-Type: application/json\r\nContent-Length: ' + str(len(json_str)) +
                    '\r\nLast-Modified: ' + last_modified +
                    '\r\nConnection: close\r\n\r\n' + json_str).encode()

        self.transport.write(http_res)
        self.transport.close()

    def connection_made(self, transport):
        self.transport = transport
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

    def data_received(self, data):
        self.h_timeout.cancel()
        self.h_timeout = asyncio.get_event_loop().call_later(
            self.timeout_sec, self.connection_timed_out)

        self.msg_buffer += data
        print(self.msg_buffer)
        asyncio.Task(self.handle_received(self.msg_buffer))

    def eof_received(self):
        pass

    def connection_lost(self, ex):
        self.h_timeout.cancel()

    def connection_timed_out(self):
        self.transport.close()

