# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_type_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_type_data.proto',
  package='msg',
  serialized_pb=_b('\n\x13msg_type_data.proto\x12\x03msg*\x8f\x01\n\ttype_data\x12\x12\n\rt_sign_up_req\x10\xf9U\x12\x12\n\rt_sign_up_ack\x10\xfaU\x12\x12\n\rt_sign_in_req\x10\xddV\x12\x12\n\rt_sign_in_ack\x10\xdeV\x12\x18\n\x13t_get_char_list_req\x10\xc1W\x12\x18\n\x13t_get_char_list_ack\x10\xc2W')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPE_DATA = _descriptor.EnumDescriptor(
  name='type_data',
  full_name='msg.type_data',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='t_sign_up_req', index=0, number=11001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='t_sign_up_ack', index=1, number=11002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='t_sign_in_req', index=2, number=11101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='t_sign_in_ack', index=3, number=11102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='t_get_char_list_req', index=4, number=11201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='t_get_char_list_ack', index=5, number=11202,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=29,
  serialized_end=172,
)
_sym_db.RegisterEnumDescriptor(_TYPE_DATA)

type_data = enum_type_wrapper.EnumTypeWrapper(_TYPE_DATA)
t_sign_up_req = 11001
t_sign_up_ack = 11002
t_sign_in_req = 11101
t_sign_in_ack = 11102
t_get_char_list_req = 11201
t_get_char_list_ack = 11202


DESCRIPTOR.enum_types_by_name['type_data'] = _TYPE_DATA


# @@protoc_insertion_point(module_scope)