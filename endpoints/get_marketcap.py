# encoding: utf-8

from pydantic import BaseModel

from helper import get_htn_price
from server import app, htnd_client


class MarketCapResponse(BaseModel):
    marketcap: int = 12000132


@app.get("/info/marketcap", response_model=MarketCapResponse | str, tags=["Hoosat Network info"])
async def get_marketcap(stringOnly: bool = False):
    """
    Get $HTN price and market cap. Price info is from coingecko.com
    """
    htn_price = await get_htn_price()
    resp = await htnd_client.request("getCoinSupplyRequest")
    mcap = round(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 100000000 * htn_price)

    if not stringOnly:
        return {
            "marketcap": mcap
        }
    else:
        if mcap < 1000000000:
            return f"{round(mcap / 1000000, 1)}M"
        else:
            return f"{round(mcap / 1000000000, 1)}B"
