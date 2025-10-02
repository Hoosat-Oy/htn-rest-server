# encoding: utf-8
import logging

from htnd.HtndThread import HtndThread


# pipenv run python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/rpc.proto ./protos/messages.proto ./protos/p2p.proto

class HtndClient(object):
    def __init__(self, htnd_host, htnd_port):
        self.htnd_host = htnd_host
        self.htnd_port = htnd_port
        self.server_version = None
        self.is_utxo_indexed = None
        self.is_synced = None
        self.p2p_id = None

    async def ping(self):
        try:
            info = await self.request("getInfoRequest")
            if not info or not info.get("getInfoResponse"):
                return False
            
            response = info["getInfoResponse"]
            self.server_version = response.get("serverVersion")
            self.is_utxo_indexed = response.get("isUtxoIndexed")
            self.is_synced = response.get("isSynced")
            self.p2p_id = response.get("p2pId")
            return info

        except Exception as exc:
            logging.error(f"Error in HtndClient.ping: {exc}")
            return False

    async def request(self, command, params=None, timeout=5):
        with HtndThread(self.htnd_host, self.htnd_port) as t:
            return await t.request(command, params, wait_for_response=True, timeout=timeout)

    async def notify(self, command, params, callback):
        t = HtndThread(self.htnd_host, self.htnd_port, async_thread=True)
        return await t.notify(command, params, callback)
