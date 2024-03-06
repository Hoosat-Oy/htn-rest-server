# encoding: utf-8

from pydantic import BaseModel
from starlette.responses import PlainTextResponse

from helper import get_htn_price, get_htn_market_data
from server import app


class PriceResponse(BaseModel):
    price: float = 0.025235


@app.get("/info/price", response_model=PriceResponse, tags=["HTN info"])
async def get_price(stringOnly: bool = False):
    """
    Returns the current price for Hoosat in USD.
    """
    if stringOnly:
        return PlainTextResponse(content=str(await get_htn_price()))

    return {"price": await get_htn_price()}


@app.get("/info/market-data",
         tags=["HTN info"],
         include_in_schema=False)
async def get_market_data():
    """
    Returns market data for htn.
    """
    return await get_htn_market_data()
