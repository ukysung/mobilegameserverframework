
import g

def handle_message_no_1(conn_id, req_msg_type, req_msg_body):
    return (conn_id, 1, b'handle_message_no_1:' + req_msg_body, True)
g.CHANNEL_HANDLERS[1] = handle_message_no_1

