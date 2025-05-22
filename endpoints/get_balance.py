# encoding: utf-8
import csv
from io import StringIO
from fastapi import Path, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List     
from sqlalchemy import asc, desc
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
        if resp is not None:
            resp = resp["getBalanceByAddressResponse"]
    except KeyError:
        if resp is not None:
            if "getUtxosByAddressesResponse" in resp and "error" in resp["getUtxosByAddressesResponse"]:
                raise HTTPException(status_code=400, detail=resp["getUtxosByAddressesResponse"]["error"])
            else:
                raise
    balance = 0
    try:
        if resp is not None:
            balance = int(resp["balance"])
    except KeyError:
        balance = 0

    return {
        "address": hoosatAddress,
        "balance": balance
    }



@app.get("/addresses/balances/json", response_model=BalanceResponses, tags=["Hoosat addresses"])
async def get_balances():
    """
    Get balances of addresses.
    """
    async with async_session() as session:  
        try:
            result = await session.execute(
                select(Balance)
                .order_by(desc(Balance.balance))
            )
            balances = result.scalars().all()
            return BalanceResponses(balances=[
                BalanceResponse(address=balance.script_public_key_address, balance=balance.balance)
                for balance in balances
            ])
        except Exception as e:
            return BalanceResponses(balances=[])


@app.get("/addresses/balances/csv", response_class=StreamingResponse, tags=["Hoosat addresses"]   )
async def get_balances_csv():
    """
    Get balances of addresses in CSV format.
    """
    async with async_session() as session: 
        try:
            result = await session.execute(
                select(Balance)
                .order_by(desc(Balance.balance))
            )
            balances = result.scalars().all()
            
            output = StringIO()
            writer = csv.writer(output)
            
            writer.writerow(["Address", "Balance"])
            
            for balance in balances:
                writer.writerow([balance.script_public_key_address, balance.balance])
            
            output.seek(0)
            
            return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=balances.csv"})
        
        except Exception as e:
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Address", "Balance"]) 
            output.seek(0)
            return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=balances.csv"})

@app.get("/addresses/balances/json/paged", response_model=BalanceResponses, tags=["Hoosat addresses"])
async def get_balances_paged(page: int = Query(1, ge=1), items_per_page: int = Query(10, ge=1)):
    """
    Get balances of addresses with pagination.
    """
    async with async_session() as session:
        try:
            result = await session.execute(
                select(Balance)
                .offset((page - 1) * items_per_page)
                .limit(items_per_page)
                .order_by(desc(Balance.balance))
            )
            balances = result.scalars().all()
            
            return BalanceResponses(
                balances=[
                    BalanceResponse(address=balance.script_public_key_address, balance=balance.balance)
                    for balance in balances
                ]
            )
        except Exception as e:
            return BalanceResponses(balances=[])


@app.get("/addresses/balances/csv/paged", response_class=StreamingResponse, tags=["Hoosat addresses"])
async def get_balances_csv_paged(page: int = Query(1, ge=1), items_per_page: int = Query(10, ge=1)):
    """
    Get balances of addresses in CSV format with pagination.
    """
    async with async_session() as session:
        try:
            result = await session.execute(
                select(Balance)
                .offset((page - 1) * items_per_page)
                .limit(items_per_page)
                .order_by(desc(Balance.balance))
            )
            balances = result.scalars().all()

            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Address", "Balance"])

            for balance in balances:
                writer.writerow([balance.script_public_key_address, balance.balance])

            output.seek(0)

            return StreamingResponse(output, media_type="text/csv", headers={
                "Content-Disposition": "attachment; filename=balances.csv"
            })

        except Exception as e:
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(["Address", "Balance"])
            output.seek(0)
            return StreamingResponse(output, media_type="text/csv", headers={
                "Content-Disposition": "attachment; filename=balances.csv"
            })
