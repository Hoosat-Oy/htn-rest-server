# encoding: utf-8

from fastapi import Path, HTTPException
from pydantic import BaseModel

from server import app, htnd_client


class BalanceResponse(BaseModel):
    address: str = "htn:pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00"
    balance: int = 38240000000


@app.get("/addresses/{htnAddress}/balance", response_model=BalanceResponse, tags=["Hoosat addresses"])
async def get_balance_from_htn_address(
        htnAddress: str = Path(
            description="Hoosat address as string e.g. htn:pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00",
            regex="^htn\:[a-z0-9]{61,63}$")):
    """
    Get balance for a given htn address
    """
    resp = await htnd_client.request("getBalanceByAddressRequest",
                                       params={
                                           "address": htnAddress
                                       })

    try:
        resp = resp["getBalanceByAddressResponse"]
    except KeyError:
        if "getUtxosByAddressesResponse" in resp and "error" in resp["getUtxosByAddressesResponse"]:
            raise HTTPException(status_code=400, detail=resp["getUtxosByAddressesResponse"]["error"])
        else:
            raise

    try:
        balance = int(resp["balance"])

    # return 0 if address is ok, but no utxos there
    except KeyError:
        balance = 0

    return {
        "address": htnAddress,
        "balance": balance
    }
