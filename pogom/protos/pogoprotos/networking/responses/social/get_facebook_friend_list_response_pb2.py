# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/get_facebook_friend_list_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_summary_pb2 as pogoprotos_dot_data_dot_player_dot_player__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/get_facebook_friend_list_response.proto',
  package='pogoprotos.networking.responses.social',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nNpogoprotos/networking/responses/social/get_facebook_friend_list_response.proto\x12&pogoprotos.networking.responses.social\x1a+pogoprotos/data/player/player_summary.proto\"\xe6\x03\n\x1dGetFacebookFriendListResponse\x12\\\n\x06result\x18\x01 \x01(\x0e\x32L.pogoprotos.networking.responses.social.GetFacebookFriendListResponse.Result\x12i\n\x06\x66riend\x18\x02 \x03(\x0b\x32Y.pogoprotos.networking.responses.social.GetFacebookFriendListResponse.FacebookFriendProto\x12\x13\n\x0bnext_cursor\x18\x03 \x01(\t\x1a_\n\x13\x46\x61\x63\x65\x62ookFriendProto\x12\x35\n\x06player\x18\x01 \x01(\x0b\x32%.pogoprotos.data.player.PlayerSummary\x12\x11\n\tfull_name\x18\x02 \x01(\t\"\x85\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x16\n\x12\x45RROR_FACEBOOK_API\x10\x03\x12\x1e\n\x1a\x45RROR_FACEBOOK_PERMISSIONS\x10\x04\x12\x18\n\x14\x45RROR_NO_FACEBOOK_ID\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__summary__pb2.DESCRIPTOR,])



_GETFACEBOOKFRIENDLISTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FACEBOOK_API', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FACEBOOK_PERMISSIONS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_FACEBOOK_ID', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_GETFACEBOOKFRIENDLISTRESPONSE_RESULT)


_GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO = _descriptor.Descriptor(
  name='FacebookFriendProto',
  full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.FacebookFriendProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.FacebookFriendProto.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.FacebookFriendProto.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=423,
  serialized_end=518,
)

_GETFACEBOOKFRIENDLISTRESPONSE = _descriptor.Descriptor(
  name='GetFacebookFriendListResponse',
  full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend', full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.friend', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_cursor', full_name='pogoprotos.networking.responses.social.GetFacebookFriendListResponse.next_cursor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO, ],
  enum_types=[
    _GETFACEBOOKFRIENDLISTRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=654,
)

_GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player_dot_player__summary__pb2._PLAYERSUMMARY
_GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO.containing_type = _GETFACEBOOKFRIENDLISTRESPONSE
_GETFACEBOOKFRIENDLISTRESPONSE.fields_by_name['result'].enum_type = _GETFACEBOOKFRIENDLISTRESPONSE_RESULT
_GETFACEBOOKFRIENDLISTRESPONSE.fields_by_name['friend'].message_type = _GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO
_GETFACEBOOKFRIENDLISTRESPONSE_RESULT.containing_type = _GETFACEBOOKFRIENDLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetFacebookFriendListResponse'] = _GETFACEBOOKFRIENDLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFacebookFriendListResponse = _reflection.GeneratedProtocolMessageType('GetFacebookFriendListResponse', (_message.Message,), dict(

  FacebookFriendProto = _reflection.GeneratedProtocolMessageType('FacebookFriendProto', (_message.Message,), dict(
    DESCRIPTOR = _GETFACEBOOKFRIENDLISTRESPONSE_FACEBOOKFRIENDPROTO,
    __module__ = 'pogoprotos.networking.responses.social.get_facebook_friend_list_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.GetFacebookFriendListResponse.FacebookFriendProto)
    ))
  ,
  DESCRIPTOR = _GETFACEBOOKFRIENDLISTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.get_facebook_friend_list_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.GetFacebookFriendListResponse)
  ))
_sym_db.RegisterMessage(GetFacebookFriendListResponse)
_sym_db.RegisterMessage(GetFacebookFriendListResponse.FacebookFriendProto)


# @@protoc_insertion_point(module_scope)