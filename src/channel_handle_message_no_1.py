
import g

def handle_message_no_1(conn_id, req_msg_type, req_msg_body):
    g.LOG.info('handle_message_no_1')
    return (conn_id, 1, b'handle_message_no_1:' + req_msg_body, g.TO_ALL)
g.CHANNEL_HANDLERS[1] = handle_message_no_1

