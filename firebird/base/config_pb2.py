# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: firebird/base/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='firebird/base/config.proto',
  package='firebird.base',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1a\x66irebird/base/config.proto\x12\rfirebird.base\x1a\x19google/protobuf/any.proto\"\xf0\x01\n\x05Value\x12\x13\n\tas_string\x18\x02 \x01(\tH\x00\x12\x12\n\x08\x61s_bytes\x18\x03 \x01(\x0cH\x00\x12\x11\n\x07\x61s_bool\x18\x04 \x01(\x08H\x00\x12\x13\n\tas_double\x18\x05 \x01(\x01H\x00\x12\x12\n\x08\x61s_float\x18\x06 \x01(\x02H\x00\x12\x13\n\tas_sint32\x18\x07 \x01(\x11H\x00\x12\x13\n\tas_sint64\x18\x08 \x01(\x12H\x00\x12\x13\n\tas_uint32\x18\t \x01(\rH\x00\x12\x13\n\tas_uint64\x18\n \x01(\x04H\x00\x12&\n\x06\x61s_msg\x18\x0b \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x06\n\x04kind\"\x93\x02\n\x0b\x43onfigProto\x12\x38\n\x07options\x18\x01 \x03(\x0b\x32\'.firebird.base.ConfigProto.OptionsEntry\x12\x38\n\x07\x63onfigs\x18\x02 \x03(\x0b\x32\'.firebird.base.ConfigProto.ConfigsEntry\x1a\x44\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.firebird.base.Value:\x02\x38\x01\x1aJ\n\x0c\x43onfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.firebird.base.ConfigProto:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='firebird.base.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='as_string', full_name='firebird.base.Value.as_string', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_bytes', full_name='firebird.base.Value.as_bytes', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_bool', full_name='firebird.base.Value.as_bool', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_double', full_name='firebird.base.Value.as_double', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_float', full_name='firebird.base.Value.as_float', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_sint32', full_name='firebird.base.Value.as_sint32', index=5,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_sint64', full_name='firebird.base.Value.as_sint64', index=6,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_uint32', full_name='firebird.base.Value.as_uint32', index=7,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_uint64', full_name='firebird.base.Value.as_uint64', index=8,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='as_msg', full_name='firebird.base.Value.as_msg', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='firebird.base.Value.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=73,
  serialized_end=313,
)


_CONFIGPROTO_OPTIONSENTRY = _descriptor.Descriptor(
  name='OptionsEntry',
  full_name='firebird.base.ConfigProto.OptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='firebird.base.ConfigProto.OptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='firebird.base.ConfigProto.OptionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=515,
)

_CONFIGPROTO_CONFIGSENTRY = _descriptor.Descriptor(
  name='ConfigsEntry',
  full_name='firebird.base.ConfigProto.ConfigsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='firebird.base.ConfigProto.ConfigsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='firebird.base.ConfigProto.ConfigsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=591,
)

_CONFIGPROTO = _descriptor.Descriptor(
  name='ConfigProto',
  full_name='firebird.base.ConfigProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='firebird.base.ConfigProto.options', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configs', full_name='firebird.base.ConfigProto.configs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGPROTO_OPTIONSENTRY, _CONFIGPROTO_CONFIGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=591,
)

_VALUE.fields_by_name['as_msg'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_string'])
_VALUE.fields_by_name['as_string'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_bytes'])
_VALUE.fields_by_name['as_bytes'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_bool'])
_VALUE.fields_by_name['as_bool'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_double'])
_VALUE.fields_by_name['as_double'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_float'])
_VALUE.fields_by_name['as_float'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_sint32'])
_VALUE.fields_by_name['as_sint32'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_sint64'])
_VALUE.fields_by_name['as_sint64'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_uint32'])
_VALUE.fields_by_name['as_uint32'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_uint64'])
_VALUE.fields_by_name['as_uint64'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['as_msg'])
_VALUE.fields_by_name['as_msg'].containing_oneof = _VALUE.oneofs_by_name['kind']
_CONFIGPROTO_OPTIONSENTRY.fields_by_name['value'].message_type = _VALUE
_CONFIGPROTO_OPTIONSENTRY.containing_type = _CONFIGPROTO
_CONFIGPROTO_CONFIGSENTRY.fields_by_name['value'].message_type = _CONFIGPROTO
_CONFIGPROTO_CONFIGSENTRY.containing_type = _CONFIGPROTO
_CONFIGPROTO.fields_by_name['options'].message_type = _CONFIGPROTO_OPTIONSENTRY
_CONFIGPROTO.fields_by_name['configs'].message_type = _CONFIGPROTO_CONFIGSENTRY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['ConfigProto'] = _CONFIGPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'firebird.base.config_pb2'
  # @@protoc_insertion_point(class_scope:firebird.base.Value)
  })
_sym_db.RegisterMessage(Value)

ConfigProto = _reflection.GeneratedProtocolMessageType('ConfigProto', (_message.Message,), {

  'OptionsEntry' : _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGPROTO_OPTIONSENTRY,
    '__module__' : 'firebird.base.config_pb2'
    # @@protoc_insertion_point(class_scope:firebird.base.ConfigProto.OptionsEntry)
    })
  ,

  'ConfigsEntry' : _reflection.GeneratedProtocolMessageType('ConfigsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGPROTO_CONFIGSENTRY,
    '__module__' : 'firebird.base.config_pb2'
    # @@protoc_insertion_point(class_scope:firebird.base.ConfigProto.ConfigsEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGPROTO,
  '__module__' : 'firebird.base.config_pb2'
  # @@protoc_insertion_point(class_scope:firebird.base.ConfigProto)
  })
_sym_db.RegisterMessage(ConfigProto)
_sym_db.RegisterMessage(ConfigProto.OptionsEntry)
_sym_db.RegisterMessage(ConfigProto.ConfigsEntry)


_CONFIGPROTO_OPTIONSENTRY._options = None
_CONFIGPROTO_CONFIGSENTRY._options = None
# @@protoc_insertion_point(module_scope)
