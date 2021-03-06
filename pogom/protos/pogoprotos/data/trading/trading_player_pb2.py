# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/trading/trading_player.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2
from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.data.trading import trading_pokemon_pb2 as pogoprotos_dot_data_dot_trading_dot_trading__pokemon__pb2
from pogoprotos.data.trading import excluded_pokemon_pb2 as pogoprotos_dot_data_dot_trading_dot_excluded__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/trading/trading_player.proto',
  package='pogoprotos.data.trading',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/data/trading/trading_player.proto\x12\x17pogoprotos.data.trading\x1a\x1fpogoprotos/inventory/loot.proto\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a-pogoprotos/data/trading/trading_pokemon.proto\x1a.pogoprotos/data/trading/excluded_pokemon.proto\"\xf6\x02\n\rTradingPlayer\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x43\n\x0epublic_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12\x42\n\x10\x65xcluded_pokemon\x18\x03 \x03(\x0b\x32(.pogoprotos.data.trading.ExcludedPokemon\x12@\n\x0ftrading_pokemon\x18\x04 \x01(\x0b\x32\'.pogoprotos.data.trading.TradingPokemon\x12)\n\x05\x62onus\x18\x05 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12)\n\x05price\x18\x06 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x1a\n\x12\x63\x61n_afford_trading\x18\x07 \x01(\x08\x12\x15\n\rhas_confirmed\x18\x08 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_trading_dot_trading__pokemon__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_trading_dot_excluded__pokemon__pb2.DESCRIPTOR,])




_TRADINGPLAYER = _descriptor.Descriptor(
  name='TradingPlayer',
  full_name='pogoprotos.data.trading.TradingPlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.data.trading.TradingPlayer.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_profile', full_name='pogoprotos.data.trading.TradingPlayer.public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excluded_pokemon', full_name='pogoprotos.data.trading.TradingPlayer.excluded_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_pokemon', full_name='pogoprotos.data.trading.TradingPlayer.trading_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bonus', full_name='pogoprotos.data.trading.TradingPlayer.bonus', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='pogoprotos.data.trading.TradingPlayer.price', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_afford_trading', full_name='pogoprotos.data.trading.TradingPlayer.can_afford_trading', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_confirmed', full_name='pogoprotos.data.trading.TradingPlayer.has_confirmed', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=254,
  serialized_end=628,
)

_TRADINGPLAYER.fields_by_name['public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_TRADINGPLAYER.fields_by_name['excluded_pokemon'].message_type = pogoprotos_dot_data_dot_trading_dot_excluded__pokemon__pb2._EXCLUDEDPOKEMON
_TRADINGPLAYER.fields_by_name['trading_pokemon'].message_type = pogoprotos_dot_data_dot_trading_dot_trading__pokemon__pb2._TRADINGPOKEMON
_TRADINGPLAYER.fields_by_name['bonus'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_TRADINGPLAYER.fields_by_name['price'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
DESCRIPTOR.message_types_by_name['TradingPlayer'] = _TRADINGPLAYER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradingPlayer = _reflection.GeneratedProtocolMessageType('TradingPlayer', (_message.Message,), dict(
  DESCRIPTOR = _TRADINGPLAYER,
  __module__ = 'pogoprotos.data.trading.trading_player_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.trading.TradingPlayer)
  ))
_sym_db.RegisterMessage(TradingPlayer)


# @@protoc_insertion_point(module_scope)
