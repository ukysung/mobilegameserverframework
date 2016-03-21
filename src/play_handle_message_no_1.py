
import g
import e

def handle_message_no_1(conn_id, req_msg_body):
    g.LOG.info('handle_message_no_1')
    return (conn_id, 1, b'handle_message_no_1:' + str(g.MST[1]).encode() + req_msg_body, e.TO_ALL)
g.PLAY_HANDLERS[1] = handle_message_no_1

