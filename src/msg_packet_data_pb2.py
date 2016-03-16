# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_packet_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import msg_error_pb2
import msg_enum_pb2
import msg_struct_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_packet_data.proto',
  package='msg',
  serialized_pb=_b('\n\x15msg_packet_data.proto\x12\x03msg\x1a\x0fmsg_error.proto\x1a\x0emsg_enum.proto\x1a\x10msg_struct.proto\"T\n\x0bsign_up_req\x12%\n\tplat_type\x18\x01 \x02(\x0e\x32\x12.msg.platform_type\x12\x0e\n\x06userid\x18\x02 \x02(\t\x12\x0e\n\x06passwd\x18\x03 \x02(\t\"B\n\x0bsign_up_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12\x12\n\nauth_token\x18\x02 \x02(\t\"T\n\x0bsign_in_req\x12%\n\tplat_type\x18\x01 \x02(\x0e\x32\x12.msg.platform_type\x12\x0e\n\x06userid\x18\x02 \x02(\t\x12\x0e\n\x06passwd\x18\x03 \x02(\t\"B\n\x0bsign_in_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12\x12\n\nauth_token\x18\x02 \x02(\t\"O\n\x14\x63reate_character_req\x12\x12\n\nauth_token\x18\x01 \x02(\t\x12\x10\n\x08\x63har_mid\x18\x02 \x02(\x05\x12\x11\n\tchar_name\x18\x03 \x02(\t\"Z\n\x14\x63reate_character_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12!\n\tchar_list\x18\x02 \x03(\x0b\x32\x0e.msg.char_info\"\'\n\x11get_char_list_req\x12\x12\n\nauth_token\x18\x01 \x02(\t\"W\n\x11get_char_list_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12!\n\tchar_list\x18\x02 \x03(\x0b\x32\x0e.msg.char_info\"7\n\x11get_item_list_req\x12\x12\n\nauth_token\x18\x01 \x02(\t\x12\x0e\n\x06\x63harid\x18\x02 \x02(\t\"W\n\x11get_item_list_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12!\n\titem_list\x18\x02 \x03(\x0b\x32\x0e.msg.item_info\"8\n\x12get_skill_list_req\x12\x12\n\nauth_token\x18\x01 \x02(\t\x12\x0e\n\x06\x63harid\x18\x02 \x02(\t\"Z\n\x12get_skill_list_ack\x12\x1f\n\x08\x65rr_code\x18\x01 \x02(\x0e\x32\r.msg.err_type\x12#\n\nskill_list\x18\x02 \x03(\x0b\x32\x0f.msg.skill_info')
  ,
  dependencies=[msg_error_pb2.DESCRIPTOR,msg_enum_pb2.DESCRIPTOR,msg_struct_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGN_UP_REQ = _descriptor.Descriptor(
  name='sign_up_req',
  full_name='msg.sign_up_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plat_type', full_name='msg.sign_up_req.plat_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userid', full_name='msg.sign_up_req.userid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='msg.sign_up_req.passwd', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=165,
)


_SIGN_UP_ACK = _descriptor.Descriptor(
  name='sign_up_ack',
  full_name='msg.sign_up_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.sign_up_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.sign_up_ack.auth_token', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=233,
)


_SIGN_IN_REQ = _descriptor.Descriptor(
  name='sign_in_req',
  full_name='msg.sign_in_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plat_type', full_name='msg.sign_in_req.plat_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userid', full_name='msg.sign_in_req.userid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='msg.sign_in_req.passwd', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=319,
)


_SIGN_IN_ACK = _descriptor.Descriptor(
  name='sign_in_ack',
  full_name='msg.sign_in_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.sign_in_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.sign_in_ack.auth_token', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=387,
)


_CREATE_CHARACTER_REQ = _descriptor.Descriptor(
  name='create_character_req',
  full_name='msg.create_character_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.create_character_req.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_mid', full_name='msg.create_character_req.char_mid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_name', full_name='msg.create_character_req.char_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=468,
)


_CREATE_CHARACTER_ACK = _descriptor.Descriptor(
  name='create_character_ack',
  full_name='msg.create_character_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.create_character_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_list', full_name='msg.create_character_ack.char_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=560,
)


_GET_CHAR_LIST_REQ = _descriptor.Descriptor(
  name='get_char_list_req',
  full_name='msg.get_char_list_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.get_char_list_req.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=601,
)


_GET_CHAR_LIST_ACK = _descriptor.Descriptor(
  name='get_char_list_ack',
  full_name='msg.get_char_list_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.get_char_list_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_list', full_name='msg.get_char_list_ack.char_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=690,
)


_GET_ITEM_LIST_REQ = _descriptor.Descriptor(
  name='get_item_list_req',
  full_name='msg.get_item_list_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.get_item_list_req.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charid', full_name='msg.get_item_list_req.charid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=692,
  serialized_end=747,
)


_GET_ITEM_LIST_ACK = _descriptor.Descriptor(
  name='get_item_list_ack',
  full_name='msg.get_item_list_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.get_item_list_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_list', full_name='msg.get_item_list_ack.item_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=836,
)


_GET_SKILL_LIST_REQ = _descriptor.Descriptor(
  name='get_skill_list_req',
  full_name='msg.get_skill_list_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_token', full_name='msg.get_skill_list_req.auth_token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charid', full_name='msg.get_skill_list_req.charid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=894,
)


_GET_SKILL_LIST_ACK = _descriptor.Descriptor(
  name='get_skill_list_ack',
  full_name='msg.get_skill_list_ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='msg.get_skill_list_ack.err_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_list', full_name='msg.get_skill_list_ack.skill_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=896,
  serialized_end=986,
)

_SIGN_UP_REQ.fields_by_name['plat_type'].enum_type = msg_enum_pb2._PLATFORM_TYPE
_SIGN_UP_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_SIGN_IN_REQ.fields_by_name['plat_type'].enum_type = msg_enum_pb2._PLATFORM_TYPE
_SIGN_IN_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_CREATE_CHARACTER_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_CREATE_CHARACTER_ACK.fields_by_name['char_list'].message_type = msg_struct_pb2._CHAR_INFO
_GET_CHAR_LIST_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_GET_CHAR_LIST_ACK.fields_by_name['char_list'].message_type = msg_struct_pb2._CHAR_INFO
_GET_ITEM_LIST_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_GET_ITEM_LIST_ACK.fields_by_name['item_list'].message_type = msg_struct_pb2._ITEM_INFO
_GET_SKILL_LIST_ACK.fields_by_name['err_code'].enum_type = msg_error_pb2._ERR_TYPE
_GET_SKILL_LIST_ACK.fields_by_name['skill_list'].message_type = msg_struct_pb2._SKILL_INFO
DESCRIPTOR.message_types_by_name['sign_up_req'] = _SIGN_UP_REQ
DESCRIPTOR.message_types_by_name['sign_up_ack'] = _SIGN_UP_ACK
DESCRIPTOR.message_types_by_name['sign_in_req'] = _SIGN_IN_REQ
DESCRIPTOR.message_types_by_name['sign_in_ack'] = _SIGN_IN_ACK
DESCRIPTOR.message_types_by_name['create_character_req'] = _CREATE_CHARACTER_REQ
DESCRIPTOR.message_types_by_name['create_character_ack'] = _CREATE_CHARACTER_ACK
DESCRIPTOR.message_types_by_name['get_char_list_req'] = _GET_CHAR_LIST_REQ
DESCRIPTOR.message_types_by_name['get_char_list_ack'] = _GET_CHAR_LIST_ACK
DESCRIPTOR.message_types_by_name['get_item_list_req'] = _GET_ITEM_LIST_REQ
DESCRIPTOR.message_types_by_name['get_item_list_ack'] = _GET_ITEM_LIST_ACK
DESCRIPTOR.message_types_by_name['get_skill_list_req'] = _GET_SKILL_LIST_REQ
DESCRIPTOR.message_types_by_name['get_skill_list_ack'] = _GET_SKILL_LIST_ACK

sign_up_req = _reflection.GeneratedProtocolMessageType('sign_up_req', (_message.Message,), dict(
  DESCRIPTOR = _SIGN_UP_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.sign_up_req)
  ))
_sym_db.RegisterMessage(sign_up_req)

sign_up_ack = _reflection.GeneratedProtocolMessageType('sign_up_ack', (_message.Message,), dict(
  DESCRIPTOR = _SIGN_UP_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.sign_up_ack)
  ))
_sym_db.RegisterMessage(sign_up_ack)

sign_in_req = _reflection.GeneratedProtocolMessageType('sign_in_req', (_message.Message,), dict(
  DESCRIPTOR = _SIGN_IN_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.sign_in_req)
  ))
_sym_db.RegisterMessage(sign_in_req)

sign_in_ack = _reflection.GeneratedProtocolMessageType('sign_in_ack', (_message.Message,), dict(
  DESCRIPTOR = _SIGN_IN_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.sign_in_ack)
  ))
_sym_db.RegisterMessage(sign_in_ack)

create_character_req = _reflection.GeneratedProtocolMessageType('create_character_req', (_message.Message,), dict(
  DESCRIPTOR = _CREATE_CHARACTER_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.create_character_req)
  ))
_sym_db.RegisterMessage(create_character_req)

create_character_ack = _reflection.GeneratedProtocolMessageType('create_character_ack', (_message.Message,), dict(
  DESCRIPTOR = _CREATE_CHARACTER_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.create_character_ack)
  ))
_sym_db.RegisterMessage(create_character_ack)

get_char_list_req = _reflection.GeneratedProtocolMessageType('get_char_list_req', (_message.Message,), dict(
  DESCRIPTOR = _GET_CHAR_LIST_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_char_list_req)
  ))
_sym_db.RegisterMessage(get_char_list_req)

get_char_list_ack = _reflection.GeneratedProtocolMessageType('get_char_list_ack', (_message.Message,), dict(
  DESCRIPTOR = _GET_CHAR_LIST_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_char_list_ack)
  ))
_sym_db.RegisterMessage(get_char_list_ack)

get_item_list_req = _reflection.GeneratedProtocolMessageType('get_item_list_req', (_message.Message,), dict(
  DESCRIPTOR = _GET_ITEM_LIST_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_item_list_req)
  ))
_sym_db.RegisterMessage(get_item_list_req)

get_item_list_ack = _reflection.GeneratedProtocolMessageType('get_item_list_ack', (_message.Message,), dict(
  DESCRIPTOR = _GET_ITEM_LIST_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_item_list_ack)
  ))
_sym_db.RegisterMessage(get_item_list_ack)

get_skill_list_req = _reflection.GeneratedProtocolMessageType('get_skill_list_req', (_message.Message,), dict(
  DESCRIPTOR = _GET_SKILL_LIST_REQ,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_skill_list_req)
  ))
_sym_db.RegisterMessage(get_skill_list_req)

get_skill_list_ack = _reflection.GeneratedProtocolMessageType('get_skill_list_ack', (_message.Message,), dict(
  DESCRIPTOR = _GET_SKILL_LIST_ACK,
  __module__ = 'msg_packet_data_pb2'
  # @@protoc_insertion_point(class_scope:msg.get_skill_list_ack)
  ))
_sym_db.RegisterMessage(get_skill_list_ack)


# @@protoc_insertion_point(module_scope)
