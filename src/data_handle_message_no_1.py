
import asyncio

@asyncio.coroutine
def handle_message_no_1(req_msg_type, req_msg_body):
    return b'handle_message_no_1:' + req_msg_body


