# encoding: utf-8
import csv
from io import StringIO
from fastapi import Path, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
from sqlalchemy.future import select

from dbsession import async_session
from endpoints import filter_fields, sql_db_only
from models.Balance import Balance

from server import app, htnd_client


class BalanceResponse(BaseModel):
    address: str = "hoosat:pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00"
    balance: int = 38240000000


class BalanceResponses(BaseModel):
    balances: List[BalanceResponse]


@app.get("/addresses/{hoosatAddress}/balance", response_model=BalanceResponse, tags=["Hoosat addresses"])
async def get_balance_from_hoosat_address(
        hoosatAddress: str = Path(
            description="Hoosat address as string e.g. hoosat:pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00",
            regex="^hoosat\:[a-z0-9]{61,63}$")):
    """
    Get balance for a given hoosat address
    """
    resp = await htnd_client.request("getBalanceByAddressRequest",
                                       params={
                                           "address": hoosatAddress
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
    except KeyError:
        balance = 0

    return {
        "address": hoosatAddress,
        "balance": balance
    }


@app.get("/balances/", response_model=BalanceResponses, tags=["Hoosat addresses"])
async def get_balances():
    """
    Get balances of addresses.
    """
    async with async_session() as session:  
        try:
            result = await session.execute(select(Balance))  
            balances = result.scalars().all()
            non_zero_balances = [balance for balance in balances if balance.balance > 0]
            sorted_balances = sorted(non_zero_balances, key=lambda balance: balance.balance, reverse=True)
            return BalanceResponses(balances=[
                BalanceResponse(address=balance.script_public_key_address, balance=balance.balance)
                for balance in sorted_balances
            ])
        except Exception as e:
            return BalanceResponses(balances=[])


@app.get("/balances-csv", response_class=StreamingResponse, tags=["Hoosat addresses"]   )
async def get_balances_csv():
    """
    Get balances of addresses in CSV format.
    """
    async with async_session() as session: 
        try:
            result = await session.execute(select(Balance))  
            balances = result.scalars().all() 
            non_zero_balances = [balance for balance in balances if balance.balance > 0]
            sorted_balances = sorted(non_zero_balances, key=lambda balance: balance.balance, reverse=True)
            
            output = StringIO()
            writer = csv.writer(output)
            
            writer.writerow(["Address", "Balance"])
            
            for balance in sorted_balances:
                writer.writerow([balance.script_public_key_address, balance.balance])
            
            output.seek(0)
            
            return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=balances.csv"})
        
        except Exception as e:
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Address", "Balance"]) 
            output.seek(0)
            return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=balances.csv"})
