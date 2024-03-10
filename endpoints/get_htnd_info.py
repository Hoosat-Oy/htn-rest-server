# encoding: utf-8
import hashlib

from pydantic import BaseModel

from server import app, htnd_client


class htndInfoResponse(BaseModel):
    mempoolSize: str = "1"
    serverVersion: str = "0.12.2"
    isUtxoIndexed: bool = True
    isSynced: bool = True
    p2pIdHashed : str = "36a17cd8644eef34fc7fe4719655e06dbdf117008900c46975e66c35acd09b01"


@app.get("/info/htnd", response_model=htndInfoResponse, tags=["Hoosat Network info"])
async def get_htnd_info():
    """
    Get some information for htnd instance, which is currently connected.
    """
    resp = await htnd_client.request("getInfoRequest")
    p2p_id = resp["getInfoResponse"].pop("p2pId")
    resp["getInfoResponse"]["p2pIdHashed"] = hashlib.sha256(p2p_id.encode()).hexdigest()
    return resp["getInfoResponse"]
