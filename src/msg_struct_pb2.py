# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_struct.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import msg_enum_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_struct.proto',
  package='msg',
  serialized_pb=_b('\n\x10msg_struct.proto\x12\x03msg\x1a\x0emsg_enum.proto\"*\n\x07vector3\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"\xe1\x02\n\tchar_info\x12\x11\n\tchar_name\x18\x01 \x02(\t\x12\x10\n\x08\x63har_mid\x18\x02 \x02(\x05\x12\x12\n\nchar_level\x18\x03 \x02(\x05\x12\x10\n\x08\x63har_exp\x18\x04 \x02(\x03\x12\x15\n\rremained_gold\x18\x05 \x02(\x05\x12\x15\n\rremained_sera\x18\x06 \x02(\x05\x12\x1c\n\x14remained_skill_point\x18\x07 \x02(\x05\x12\x14\n\x0c\x65quip_weapon\x18\x08 \x02(\x05\x12\x12\n\nequip_head\x18\t \x02(\x05\x12\x12\n\nequip_body\x18\n \x02(\x05\x12\x13\n\x0b\x65quip_wings\x18\x0b \x02(\x05\x12\x13\n\x0bskill_slot1\x18\x0c \x02(\x05\x12\x13\n\x0bskill_slot2\x18\r \x02(\x05\x12\x13\n\x0bskill_slot3\x18\x0e \x02(\x05\x12\x13\n\x0bskill_slot4\x18\x0f \x02(\x05\x12\x16\n\x0elast_logintime\x18\x10 \x02(\x03\"T\n\titem_info\x12\x11\n\tinven_seq\x18\x01 \x02(\x04\x12\"\n\nequip_part\x18\x02 \x02(\x0e\x32\x0e.msg.part_type\x12\x10\n\x08item_mid\x18\x03 \x02(\x05\"\x1f\n\nskill_info\x12\x11\n\tskill_mid\x18\x01 \x02(\x05')
  ,
  dependencies=[msg_enum_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VECTOR3 = _descriptor.Descriptor(
  name='vector3',
  full_name='msg.vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='msg.vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='msg.vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='msg.vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=41,
  serialized_end=83,
)


_CHAR_INFO = _descriptor.Descriptor(
  name='char_info',
  full_name='msg.char_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='char_name', full_name='msg.char_info.char_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_mid', full_name='msg.char_info.char_mid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_level', full_name='msg.char_info.char_level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='char_exp', full_name='msg.char_info.char_exp', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remained_gold', full_name='msg.char_info.remained_gold', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remained_sera', full_name='msg.char_info.remained_sera', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remained_skill_point', full_name='msg.char_info.remained_skill_point', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_weapon', full_name='msg.char_info.equip_weapon', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_head', full_name='msg.char_info.equip_head', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_body', full_name='msg.char_info.equip_body', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_wings', full_name='msg.char_info.equip_wings', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_slot1', full_name='msg.char_info.skill_slot1', index=11,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_slot2', full_name='msg.char_info.skill_slot2', index=12,
      number=13, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_slot3', full_name='msg.char_info.skill_slot3', index=13,
      number=14, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skill_slot4', full_name='msg.char_info.skill_slot4', index=14,
      number=15, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_logintime', full_name='msg.char_info.last_logintime', index=15,
      number=16, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=86,
  serialized_end=439,
)


_ITEM_INFO = _descriptor.Descriptor(
  name='item_info',
  full_name='msg.item_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inven_seq', full_name='msg.item_info.inven_seq', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equip_part', full_name='msg.item_info.equip_part', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_mid', full_name='msg.item_info.item_mid', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=441,
  serialized_end=525,
)


_SKILL_INFO = _descriptor.Descriptor(
  name='skill_info',
  full_name='msg.skill_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skill_mid', full_name='msg.skill_info.skill_mid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=527,
  serialized_end=558,
)

_ITEM_INFO.fields_by_name['equip_part'].enum_type = msg_enum_pb2._PART_TYPE
DESCRIPTOR.message_types_by_name['vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['char_info'] = _CHAR_INFO
DESCRIPTOR.message_types_by_name['item_info'] = _ITEM_INFO
DESCRIPTOR.message_types_by_name['skill_info'] = _SKILL_INFO

vector3 = _reflection.GeneratedProtocolMessageType('vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.vector3)
  ))
_sym_db.RegisterMessage(vector3)

char_info = _reflection.GeneratedProtocolMessageType('char_info', (_message.Message,), dict(
  DESCRIPTOR = _CHAR_INFO,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.char_info)
  ))
_sym_db.RegisterMessage(char_info)

item_info = _reflection.GeneratedProtocolMessageType('item_info', (_message.Message,), dict(
  DESCRIPTOR = _ITEM_INFO,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.item_info)
  ))
_sym_db.RegisterMessage(item_info)

skill_info = _reflection.GeneratedProtocolMessageType('skill_info', (_message.Message,), dict(
  DESCRIPTOR = _SKILL_INFO,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:msg.skill_info)
  ))
_sym_db.RegisterMessage(skill_info)


# @@protoc_insertion_point(module_scope)
