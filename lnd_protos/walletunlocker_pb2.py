# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: walletunlocker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import lightning_pb2 as lightning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14walletunlocker.proto\x12\x05lnrpc\x1a\x0flightning.proto\"A\n\x0eGenSeedRequest\x12\x19\n\x11\x61\x65zeed_passphrase\x18\x01 \x01(\x0c\x12\x14\n\x0cseed_entropy\x18\x02 \x01(\x0c\"H\n\x0fGenSeedResponse\x12\x1c\n\x14\x63ipher_seed_mnemonic\x18\x01 \x03(\t\x12\x17\n\x0f\x65nciphered_seed\x18\x02 \x01(\x0c\"\xd8\x02\n\x11InitWalletRequest\x12\x17\n\x0fwallet_password\x18\x01 \x01(\x0c\x12\x1c\n\x14\x63ipher_seed_mnemonic\x18\x02 \x03(\t\x12\x19\n\x11\x61\x65zeed_passphrase\x18\x03 \x01(\x0c\x12\x17\n\x0frecovery_window\x18\x04 \x01(\x05\x12\x32\n\x0f\x63hannel_backups\x18\x05 \x01(\x0b\x32\x19.lnrpc.ChanBackupSnapshot\x12\x16\n\x0estateless_init\x18\x06 \x01(\x08\x12\x1b\n\x13\x65xtended_master_key\x18\x07 \x01(\t\x12.\n&extended_master_key_birthday_timestamp\x18\x08 \x01(\x04\x12$\n\nwatch_only\x18\t \x01(\x0b\x32\x10.lnrpc.WatchOnly\x12\x19\n\x11macaroon_root_key\x18\n \x01(\x0c\",\n\x12InitWalletResponse\x12\x16\n\x0e\x61\x64min_macaroon\x18\x01 \x01(\x0c\"}\n\tWatchOnly\x12%\n\x1dmaster_key_birthday_timestamp\x18\x01 \x01(\x04\x12\x1e\n\x16master_key_fingerprint\x18\x02 \x01(\x0c\x12)\n\x08\x61\x63\x63ounts\x18\x03 \x03(\x0b\x32\x17.lnrpc.WatchOnlyAccount\"U\n\x10WatchOnlyAccount\x12\x0f\n\x07purpose\x18\x01 \x01(\r\x12\x11\n\tcoin_type\x18\x02 \x01(\r\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\r\x12\x0c\n\x04xpub\x18\x04 \x01(\t\"\x93\x01\n\x13UnlockWalletRequest\x12\x17\n\x0fwallet_password\x18\x01 \x01(\x0c\x12\x17\n\x0frecovery_window\x18\x02 \x01(\x05\x12\x32\n\x0f\x63hannel_backups\x18\x03 \x01(\x0b\x32\x19.lnrpc.ChanBackupSnapshot\x12\x16\n\x0estateless_init\x18\x04 \x01(\x08\"\x16\n\x14UnlockWalletResponse\"~\n\x15\x43hangePasswordRequest\x12\x18\n\x10\x63urrent_password\x18\x01 \x01(\x0c\x12\x14\n\x0cnew_password\x18\x02 \x01(\x0c\x12\x16\n\x0estateless_init\x18\x03 \x01(\x08\x12\x1d\n\x15new_macaroon_root_key\x18\x04 \x01(\x08\"0\n\x16\x43hangePasswordResponse\x12\x16\n\x0e\x61\x64min_macaroon\x18\x01 \x01(\x0c\x32\xa5\x02\n\x0eWalletUnlocker\x12\x38\n\x07GenSeed\x12\x15.lnrpc.GenSeedRequest\x1a\x16.lnrpc.GenSeedResponse\x12\x41\n\nInitWallet\x12\x18.lnrpc.InitWalletRequest\x1a\x19.lnrpc.InitWalletResponse\x12G\n\x0cUnlockWallet\x12\x1a.lnrpc.UnlockWalletRequest\x1a\x1b.lnrpc.UnlockWalletResponse\x12M\n\x0e\x43hangePassword\x12\x1c.lnrpc.ChangePasswordRequest\x1a\x1d.lnrpc.ChangePasswordResponseB\'Z%github.com/lightningnetwork/lnd/lnrpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'walletunlocker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z%github.com/lightningnetwork/lnd/lnrpc'
  _GENSEEDREQUEST._serialized_start=48
  _GENSEEDREQUEST._serialized_end=113
  _GENSEEDRESPONSE._serialized_start=115
  _GENSEEDRESPONSE._serialized_end=187
  _INITWALLETREQUEST._serialized_start=190
  _INITWALLETREQUEST._serialized_end=534
  _INITWALLETRESPONSE._serialized_start=536
  _INITWALLETRESPONSE._serialized_end=580
  _WATCHONLY._serialized_start=582
  _WATCHONLY._serialized_end=707
  _WATCHONLYACCOUNT._serialized_start=709
  _WATCHONLYACCOUNT._serialized_end=794
  _UNLOCKWALLETREQUEST._serialized_start=797
  _UNLOCKWALLETREQUEST._serialized_end=944
  _UNLOCKWALLETRESPONSE._serialized_start=946
  _UNLOCKWALLETRESPONSE._serialized_end=968
  _CHANGEPASSWORDREQUEST._serialized_start=970
  _CHANGEPASSWORDREQUEST._serialized_end=1096
  _CHANGEPASSWORDRESPONSE._serialized_start=1098
  _CHANGEPASSWORDRESPONSE._serialized_end=1146
  _WALLETUNLOCKER._serialized_start=1149
  _WALLETUNLOCKER._serialized_end=1442
# @@protoc_insertion_point(module_scope)
