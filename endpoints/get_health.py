# encoding: utf-8
import hashlib
from datetime import datetime, timedelta
from typing import List

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select

from dbsession import async_session
from models.Transaction import Transaction
from server import app, htnd_client


class HtndResponse(BaseModel):
    htndHost: str = ""
    serverVersion: str = "0.12.6"
    isUtxoIndexed: bool = True
    isSynced: bool = True
    p2pId: str = "1231312"


class HealthResponse(BaseModel):
    htndServers: List[HtndResponse]


@app.get("/info/health", response_model=HealthResponse, tags=["Hoosat network info"])
async def health_state():
    """
    Returns the current hashrate for Hoosat network in TH/s.
    """
    await htnd_client.initialize_all()

    htnds = []

    async with async_session() as s:
        last_block_time = (await s.execute(select(Transaction.block_time)
                                           .limit(1)
                                           .order_by(Transaction.block_time.desc()))).scalar()

    time_diff = datetime.now() - datetime.fromtimestamp(last_block_time / 1000)

    if time_diff > timedelta(minutes=10):
        raise HTTPException(status_code=500, detail="Transactions not up to date")

    for i, htnd_info in enumerate(htnd_client.htnds):
        htnds.append({
            "isSynced": htnd_info.is_synced if htnd_info.is_synced is not None else False,
            "isUtxoIndexed": htnd_info.is_utxo_indexed if htnd_info.is_utxo_indexed is not None else False,
            "p2pId": hashlib.sha256((htnd_info.p2p_id or "").encode()).hexdigest(),
            "htndHost": f"HTND_HOST_{i + 1}",
            "serverVersion": htnd_info.server_version or "unknown"
        })

    return {
        "htndServers": htnds
    }
