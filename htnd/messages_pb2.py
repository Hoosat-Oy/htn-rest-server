# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

try:
  from . import p2p_pb2 as p2p__pb2
  from . import rpc_pb2 as rpc__pb2
except ImportError:
  import p2p_pb2 as p2p__pb2
  import rpc_pb2 as rpc__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\tprotowire\x1a\tp2p.proto\x1a\trpc.proto\"\xd1R\n\rHoosatdMessage\x12\x30\n\taddresses\x18\x01 \x01(\x0b\x32\x1b.protowire.AddressesMessageH\x00\x12(\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.protowire.BlockMessageH\x00\x12\x34\n\x0btransaction\x18\x03 \x01(\x0b\x32\x1d.protowire.TransactionMessageH\x00\x12\x36\n\x0c\x62lockLocator\x18\x05 \x01(\x0b\x32\x1e.protowire.BlockLocatorMessageH\x00\x12>\n\x10requestAddresses\x18\x06 \x01(\x0b\x32\".protowire.RequestAddressesMessageH\x00\x12\x42\n\x12requestRelayBlocks\x18\n \x01(\x0b\x32$.protowire.RequestRelayBlocksMessageH\x00\x12\x44\n\x13requestTransactions\x18\x0c \x01(\x0b\x32%.protowire.RequestTransactionsMessageH\x00\x12+\n\x08ibdBlock\x18\r \x01(\x0b\x32\x17.protowire.BlockMessageH\x00\x12\x38\n\rinvRelayBlock\x18\x0e \x01(\x0b\x32\x1f.protowire.InvRelayBlockMessageH\x00\x12<\n\x0finvTransactions\x18\x0f \x01(\x0b\x32!.protowire.InvTransactionsMessageH\x00\x12&\n\x04ping\x18\x10 \x01(\x0b\x32\x16.protowire.PingMessageH\x00\x12&\n\x04pong\x18\x11 \x01(\x0b\x32\x16.protowire.PongMessageH\x00\x12*\n\x06verack\x18\x13 \x01(\x0b\x32\x18.protowire.VerackMessageH\x00\x12,\n\x07version\x18\x14 \x01(\x0b\x32\x19.protowire.VersionMessageH\x00\x12\x44\n\x13transactionNotFound\x18\x15 \x01(\x0b\x32%.protowire.TransactionNotFoundMessageH\x00\x12*\n\x06reject\x18\x16 \x01(\x0b\x32\x18.protowire.RejectMessageH\x00\x12N\n\x18pruningPointUtxoSetChunk\x18\x19 \x01(\x0b\x32*.protowire.PruningPointUtxoSetChunkMessageH\x00\x12>\n\x10requestIBDBlocks\x18\x1a \x01(\x0b\x32\".protowire.RequestIBDBlocksMessageH\x00\x12J\n\x16unexpectedPruningPoint\x18\x1b \x01(\x0b\x32(.protowire.UnexpectedPruningPointMessageH\x00\x12<\n\x0fibdBlockLocator\x18\x1e \x01(\x0b\x32!.protowire.IbdBlockLocatorMessageH\x00\x12R\n\x1aibdBlockLocatorHighestHash\x18\x1f \x01(\x0b\x32,.protowire.IbdBlockLocatorHighestHashMessageH\x00\x12\x64\n#requestNextPruningPointUtxoSetChunk\x18! \x01(\x0b\x32\x35.protowire.RequestNextPruningPointUtxoSetChunkMessageH\x00\x12X\n\x1d\x64onePruningPointUtxoSetChunks\x18\" \x01(\x0b\x32/.protowire.DonePruningPointUtxoSetChunksMessageH\x00\x12\x62\n\"ibdBlockLocatorHighestHashNotFound\x18# \x01(\x0b\x32\x34.protowire.IbdBlockLocatorHighestHashNotFoundMessageH\x00\x12\x46\n\x14\x62lockWithTrustedData\x18$ \x01(\x0b\x32&.protowire.BlockWithTrustedDataMessageH\x00\x12P\n\x19\x64oneBlocksWithTrustedData\x18% \x01(\x0b\x32+.protowire.DoneBlocksWithTrustedDataMessageH\x00\x12`\n!requestPruningPointAndItsAnticone\x18( \x01(\x0b\x32\x33.protowire.RequestPruningPointAndItsAnticoneMessageH\x00\x12\x36\n\x0c\x62lockHeaders\x18) \x01(\x0b\x32\x1e.protowire.BlockHeadersMessageH\x00\x12\x42\n\x12requestNextHeaders\x18* \x01(\x0b\x32$.protowire.RequestNextHeadersMessageH\x00\x12\x34\n\x0b\x44oneHeaders\x18+ \x01(\x0b\x32\x1d.protowire.DoneHeadersMessageH\x00\x12R\n\x1arequestPruningPointUTXOSet\x18, \x01(\x0b\x32,.protowire.RequestPruningPointUTXOSetMessageH\x00\x12:\n\x0erequestHeaders\x18- \x01(\x0b\x32 .protowire.RequestHeadersMessageH\x00\x12\x44\n\x13requestBlockLocator\x18. \x01(\x0b\x32%.protowire.RequestBlockLocatorMessageH\x00\x12\x38\n\rpruningPoints\x18/ \x01(\x0b\x32\x1f.protowire.PruningPointsMessageH\x00\x12N\n\x18requestPruningPointProof\x18\x30 \x01(\x0b\x32*.protowire.RequestPruningPointProofMessageH\x00\x12@\n\x11pruningPointProof\x18\x31 \x01(\x0b\x32#.protowire.PruningPointProofMessageH\x00\x12(\n\x05ready\x18\x32 \x01(\x0b\x32\x17.protowire.ReadyMessageH\x00\x12J\n\x16\x62lockWithTrustedDataV4\x18\x33 \x01(\x0b\x32(.protowire.BlockWithTrustedDataV4MessageH\x00\x12\x34\n\x0btrustedData\x18\x34 \x01(\x0b\x32\x1d.protowire.TrustedDataMessageH\x00\x12T\n\x1brequestIBDChainBlockLocator\x18\x35 \x01(\x0b\x32-.protowire.RequestIBDChainBlockLocatorMessageH\x00\x12\x46\n\x14ibdChainBlockLocator\x18\x36 \x01(\x0b\x32&.protowire.IbdChainBlockLocatorMessageH\x00\x12<\n\x0frequestAnticone\x18\x37 \x01(\x0b\x32!.protowire.RequestAnticoneMessageH\x00\x12t\n+requestNextPruningPointAndItsAnticoneBlocks\x18\x38 \x01(\x0b\x32=.protowire.RequestNextPruningPointAndItsAnticoneBlocksMessageH\x00\x12O\n\x18getCurrentNetworkRequest\x18\xe9\x07 \x01(\x0b\x32*.protowire.GetCurrentNetworkRequestMessageH\x00\x12Q\n\x19getCurrentNetworkResponse\x18\xea\x07 \x01(\x0b\x32+.protowire.GetCurrentNetworkResponseMessageH\x00\x12\x43\n\x12submitBlockRequest\x18\xeb\x07 \x01(\x0b\x32$.protowire.SubmitBlockRequestMessageH\x00\x12\x45\n\x13submitBlockResponse\x18\xec\x07 \x01(\x0b\x32%.protowire.SubmitBlockResponseMessageH\x00\x12M\n\x17getBlockTemplateRequest\x18\xed\x07 \x01(\x0b\x32).protowire.GetBlockTemplateRequestMessageH\x00\x12O\n\x18getBlockTemplateResponse\x18\xee\x07 \x01(\x0b\x32*.protowire.GetBlockTemplateResponseMessageH\x00\x12M\n\x17notifyBlockAddedRequest\x18\xef\x07 \x01(\x0b\x32).protowire.NotifyBlockAddedRequestMessageH\x00\x12O\n\x18notifyBlockAddedResponse\x18\xf0\x07 \x01(\x0b\x32*.protowire.NotifyBlockAddedResponseMessageH\x00\x12K\n\x16\x62lockAddedNotification\x18\xf1\x07 \x01(\x0b\x32(.protowire.BlockAddedNotificationMessageH\x00\x12M\n\x17getPeerAddressesRequest\x18\xf2\x07 \x01(\x0b\x32).protowire.GetPeerAddressesRequestMessageH\x00\x12O\n\x18getPeerAddressesResponse\x18\xf3\x07 \x01(\x0b\x32*.protowire.GetPeerAddressesResponseMessageH\x00\x12Q\n\x19getSelectedTipHashRequest\x18\xf4\x07 \x01(\x0b\x32+.protowire.GetSelectedTipHashRequestMessageH\x00\x12S\n\x1agetSelectedTipHashResponse\x18\xf5\x07 \x01(\x0b\x32,.protowire.GetSelectedTipHashResponseMessageH\x00\x12K\n\x16getMempoolEntryRequest\x18\xf6\x07 \x01(\x0b\x32(.protowire.GetMempoolEntryRequestMessageH\x00\x12M\n\x17getMempoolEntryResponse\x18\xf7\x07 \x01(\x0b\x32).protowire.GetMempoolEntryResponseMessageH\x00\x12U\n\x1bgetConnectedPeerInfoRequest\x18\xf8\x07 \x01(\x0b\x32-.protowire.GetConnectedPeerInfoRequestMessageH\x00\x12W\n\x1cgetConnectedPeerInfoResponse\x18\xf9\x07 \x01(\x0b\x32..protowire.GetConnectedPeerInfoResponseMessageH\x00\x12;\n\x0e\x61\x64\x64PeerRequest\x18\xfa\x07 \x01(\x0b\x32 .protowire.AddPeerRequestMessageH\x00\x12=\n\x0f\x61\x64\x64PeerResponse\x18\xfb\x07 \x01(\x0b\x32!.protowire.AddPeerResponseMessageH\x00\x12O\n\x18submitTransactionRequest\x18\xfc\x07 \x01(\x0b\x32*.protowire.SubmitTransactionRequestMessageH\x00\x12Q\n\x19submitTransactionResponse\x18\xfd\x07 \x01(\x0b\x32+.protowire.SubmitTransactionResponseMessageH\x00\x12{\n.notifyVirtualSelectedParentChainChangedRequest\x18\xfe\x07 \x01(\x0b\x32@.protowire.NotifyVirtualSelectedParentChainChangedRequestMessageH\x00\x12}\n/notifyVirtualSelectedParentChainChangedResponse\x18\xff\x07 \x01(\x0b\x32\x41.protowire.NotifyVirtualSelectedParentChainChangedResponseMessageH\x00\x12y\n-virtualSelectedParentChainChangedNotification\x18\x80\x08 \x01(\x0b\x32?.protowire.VirtualSelectedParentChainChangedNotificationMessageH\x00\x12=\n\x0fgetBlockRequest\x18\x81\x08 \x01(\x0b\x32!.protowire.GetBlockRequestMessageH\x00\x12?\n\x10getBlockResponse\x18\x82\x08 \x01(\x0b\x32\".protowire.GetBlockResponseMessageH\x00\x12G\n\x14getSubnetworkRequest\x18\x83\x08 \x01(\x0b\x32&.protowire.GetSubnetworkRequestMessageH\x00\x12I\n\x15getSubnetworkResponse\x18\x84\x08 \x01(\x0b\x32\'.protowire.GetSubnetworkResponseMessageH\x00\x12y\n-getVirtualSelectedParentChainFromBlockRequest\x18\x85\x08 \x01(\x0b\x32?.protowire.GetVirtualSelectedParentChainFromBlockRequestMessageH\x00\x12{\n.getVirtualSelectedParentChainFromBlockResponse\x18\x86\x08 \x01(\x0b\x32@.protowire.GetVirtualSelectedParentChainFromBlockResponseMessageH\x00\x12?\n\x10getBlocksRequest\x18\x87\x08 \x01(\x0b\x32\".protowire.GetBlocksRequestMessageH\x00\x12\x41\n\x11getBlocksResponse\x18\x88\x08 \x01(\x0b\x32#.protowire.GetBlocksResponseMessageH\x00\x12G\n\x14getBlockCountRequest\x18\x89\x08 \x01(\x0b\x32&.protowire.GetBlockCountRequestMessageH\x00\x12I\n\x15getBlockCountResponse\x18\x8a\x08 \x01(\x0b\x32\'.protowire.GetBlockCountResponseMessageH\x00\x12K\n\x16getBlockDagInfoRequest\x18\x8b\x08 \x01(\x0b\x32(.protowire.GetBlockDagInfoRequestMessageH\x00\x12M\n\x17getBlockDagInfoResponse\x18\x8c\x08 \x01(\x0b\x32).protowire.GetBlockDagInfoResponseMessageH\x00\x12[\n\x1eresolveFinalityConflictRequest\x18\x8d\x08 \x01(\x0b\x32\x30.protowire.ResolveFinalityConflictRequestMessageH\x00\x12]\n\x1fresolveFinalityConflictResponse\x18\x8e\x08 \x01(\x0b\x32\x31.protowire.ResolveFinalityConflictResponseMessageH\x00\x12[\n\x1enotifyFinalityConflictsRequest\x18\x8f\x08 \x01(\x0b\x32\x30.protowire.NotifyFinalityConflictsRequestMessageH\x00\x12]\n\x1fnotifyFinalityConflictsResponse\x18\x90\x08 \x01(\x0b\x32\x31.protowire.NotifyFinalityConflictsResponseMessageH\x00\x12W\n\x1c\x66inalityConflictNotification\x18\x91\x08 \x01(\x0b\x32..protowire.FinalityConflictNotificationMessageH\x00\x12g\n$finalityConflictResolvedNotification\x18\x92\x08 \x01(\x0b\x32\x36.protowire.FinalityConflictResolvedNotificationMessageH\x00\x12O\n\x18getMempoolEntriesRequest\x18\x93\x08 \x01(\x0b\x32*.protowire.GetMempoolEntriesRequestMessageH\x00\x12Q\n\x19getMempoolEntriesResponse\x18\x94\x08 \x01(\x0b\x32+.protowire.GetMempoolEntriesResponseMessageH\x00\x12=\n\x0fshutDownRequest\x18\x95\x08 \x01(\x0b\x32!.protowire.ShutDownRequestMessageH\x00\x12?\n\x10shutDownResponse\x18\x96\x08 \x01(\x0b\x32\".protowire.ShutDownResponseMessageH\x00\x12\x41\n\x11getHeadersRequest\x18\x97\x08 \x01(\x0b\x32#.protowire.GetHeadersRequestMessageH\x00\x12\x43\n\x12getHeadersResponse\x18\x98\x08 \x01(\x0b\x32$.protowire.GetHeadersResponseMessageH\x00\x12Q\n\x19notifyUtxosChangedRequest\x18\x99\x08 \x01(\x0b\x32+.protowire.NotifyUtxosChangedRequestMessageH\x00\x12S\n\x1anotifyUtxosChangedResponse\x18\x9a\x08 \x01(\x0b\x32,.protowire.NotifyUtxosChangedResponseMessageH\x00\x12O\n\x18utxosChangedNotification\x18\x9b\x08 \x01(\x0b\x32*.protowire.UtxosChangedNotificationMessageH\x00\x12S\n\x1agetUtxosByAddressesRequest\x18\x9c\x08 \x01(\x0b\x32,.protowire.GetUtxosByAddressesRequestMessageH\x00\x12U\n\x1bgetUtxosByAddressesResponse\x18\x9d\x08 \x01(\x0b\x32-.protowire.GetUtxosByAddressesResponseMessageH\x00\x12o\n(getVirtualSelectedParentBlueScoreRequest\x18\x9e\x08 \x01(\x0b\x32:.protowire.GetVirtualSelectedParentBlueScoreRequestMessageH\x00\x12q\n)getVirtualSelectedParentBlueScoreResponse\x18\x9f\x08 \x01(\x0b\x32;.protowire.GetVirtualSelectedParentBlueScoreResponseMessageH\x00\x12\x83\x01\n2notifyVirtualSelectedParentBlueScoreChangedRequest\x18\xa0\x08 \x01(\x0b\x32\x44.protowire.NotifyVirtualSelectedParentBlueScoreChangedRequestMessageH\x00\x12\x85\x01\n3notifyVirtualSelectedParentBlueScoreChangedResponse\x18\xa1\x08 \x01(\x0b\x32\x45.protowire.NotifyVirtualSelectedParentBlueScoreChangedResponseMessageH\x00\x12\x81\x01\n1virtualSelectedParentBlueScoreChangedNotification\x18\xa2\x08 \x01(\x0b\x32\x43.protowire.VirtualSelectedParentBlueScoreChangedNotificationMessageH\x00\x12\x33\n\nbanRequest\x18\xa3\x08 \x01(\x0b\x32\x1c.protowire.BanRequestMessageH\x00\x12\x35\n\x0b\x62\x61nResponse\x18\xa4\x08 \x01(\x0b\x32\x1d.protowire.BanResponseMessageH\x00\x12\x37\n\x0cunbanRequest\x18\xa5\x08 \x01(\x0b\x32\x1e.protowire.UnbanRequestMessageH\x00\x12\x39\n\runbanResponse\x18\xa6\x08 \x01(\x0b\x32\x1f.protowire.UnbanResponseMessageH\x00\x12;\n\x0egetInfoRequest\x18\xa7\x08 \x01(\x0b\x32 .protowire.GetInfoRequestMessageH\x00\x12=\n\x0fgetInfoResponse\x18\xa8\x08 \x01(\x0b\x32!.protowire.GetInfoResponseMessageH\x00\x12_\n stopNotifyingUtxosChangedRequest\x18\xa9\x08 \x01(\x0b\x32\x32.protowire.StopNotifyingUtxosChangedRequestMessageH\x00\x12\x61\n!stopNotifyingUtxosChangedResponse\x18\xaa\x08 \x01(\x0b\x32\x33.protowire.StopNotifyingUtxosChangedResponseMessageH\x00\x12o\n(notifyPruningPointUTXOSetOverrideRequest\x18\xab\x08 \x01(\x0b\x32:.protowire.NotifyPruningPointUTXOSetOverrideRequestMessageH\x00\x12q\n)notifyPruningPointUTXOSetOverrideResponse\x18\xac\x08 \x01(\x0b\x32;.protowire.NotifyPruningPointUTXOSetOverrideResponseMessageH\x00\x12m\n\'pruningPointUTXOSetOverrideNotification\x18\xad\x08 \x01(\x0b\x32\x39.protowire.PruningPointUTXOSetOverrideNotificationMessageH\x00\x12}\n/stopNotifyingPruningPointUTXOSetOverrideRequest\x18\xae\x08 \x01(\x0b\x32\x41.protowire.StopNotifyingPruningPointUTXOSetOverrideRequestMessageH\x00\x12\x7f\n0stopNotifyingPruningPointUTXOSetOverrideResponse\x18\xaf\x08 \x01(\x0b\x32\x42.protowire.StopNotifyingPruningPointUTXOSetOverrideResponseMessageH\x00\x12i\n%estimateNetworkHashesPerSecondRequest\x18\xb0\x08 \x01(\x0b\x32\x37.protowire.EstimateNetworkHashesPerSecondRequestMessageH\x00\x12k\n&estimateNetworkHashesPerSecondResponse\x18\xb1\x08 \x01(\x0b\x32\x38.protowire.EstimateNetworkHashesPerSecondResponseMessageH\x00\x12\x65\n#notifyVirtualDaaScoreChangedRequest\x18\xb2\x08 \x01(\x0b\x32\x35.protowire.NotifyVirtualDaaScoreChangedRequestMessageH\x00\x12g\n$notifyVirtualDaaScoreChangedResponse\x18\xb3\x08 \x01(\x0b\x32\x36.protowire.NotifyVirtualDaaScoreChangedResponseMessageH\x00\x12\x63\n\"virtualDaaScoreChangedNotification\x18\xb4\x08 \x01(\x0b\x32\x34.protowire.VirtualDaaScoreChangedNotificationMessageH\x00\x12S\n\x1agetBalanceByAddressRequest\x18\xb5\x08 \x01(\x0b\x32,.protowire.GetBalanceByAddressRequestMessageH\x00\x12U\n\x1bgetBalanceByAddressResponse\x18\xb6\x08 \x01(\x0b\x32-.protowire.GetBalanceByAddressResponseMessageH\x00\x12Y\n\x1dgetBalancesByAddressesRequest\x18\xb7\x08 \x01(\x0b\x32/.protowire.GetBalancesByAddressesRequestMessageH\x00\x12[\n\x1egetBalancesByAddressesResponse\x18\xb8\x08 \x01(\x0b\x32\x30.protowire.GetBalancesByAddressesResponseMessageH\x00\x12Y\n\x1dnotifyNewBlockTemplateRequest\x18\xb9\x08 \x01(\x0b\x32/.protowire.NotifyNewBlockTemplateRequestMessageH\x00\x12[\n\x1enotifyNewBlockTemplateResponse\x18\xba\x08 \x01(\x0b\x32\x30.protowire.NotifyNewBlockTemplateResponseMessageH\x00\x12W\n\x1cnewBlockTemplateNotification\x18\xbb\x08 \x01(\x0b\x32..protowire.NewBlockTemplateNotificationMessageH\x00\x12\x65\n#getMempoolEntriesByAddressesRequest\x18\xbc\x08 \x01(\x0b\x32\x35.protowire.GetMempoolEntriesByAddressesRequestMessageH\x00\x12g\n$getMempoolEntriesByAddressesResponse\x18\xbd\x08 \x01(\x0b\x32\x36.protowire.GetMempoolEntriesByAddressesResponseMessageH\x00\x12G\n\x14getCoinSupplyRequest\x18\xbe\x08 \x01(\x0b\x32&.protowire.GetCoinSupplyRequestMessageH\x00\x12I\n\x15getCoinSupplyResponse\x18\xbf\x08 \x01(\x0b\x32\'.protowire.GetCoinSupplyResponseMessageH\x00\x42\t\n\x07payload2P\n\x03P2P\x12I\n\rMessageStream\x12\x18.protowire.HoosatdMessage\x1a\x18.protowire.HoosatdMessage\"\x00(\x01\x30\x01\x32P\n\x03RPC\x12I\n\rMessageStream\x12\x18.protowire.HoosatdMessage\x1a\x18.protowire.HoosatdMessage\"\x00(\x01\x30\x01\x42&Z$github.com/htnpanet/htnpad/protowireb\x06proto3')



_HTNPADMESSAGE = DESCRIPTOR.message_types_by_name['HoosatdMessage']
HoosatdMessage = _reflection.GeneratedProtocolMessageType('HoosatdMessage', (_message.Message,), {
  'DESCRIPTOR' : _HTNPADMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:protowire.HoosatdMessage)
  })
_sym_db.RegisterMessage(HoosatdMessage)

_P2P = DESCRIPTOR.services_by_name['P2P']
_RPC = DESCRIPTOR.services_by_name['RPC']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/htnpanet/htnpad/protowire'
  _HTNPADMESSAGE._serialized_start=52
  _HTNPADMESSAGE._serialized_end=10629
  _P2P._serialized_start=10631
  _P2P._serialized_end=10711
  _RPC._serialized_start=10713
  _RPC._serialized_end=10793
# @@protoc_insertion_point(module_scope)
