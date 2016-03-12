
import struct

#struct
#{
#	int32_t msg_type; // 4 bytes
#	int32_t msg_size; // 4 bytes
#}
# totally 8 bytes
HEADER_SIZE = 8

def unpack_head(msg_head):
    return struct.unpack('ii', msg_head)

def pack(msg_type, msg):
    msg_str = msg.SerializeToString()
    return struct.pack('ii', msg_type, len(msg_str)) + msg_str

