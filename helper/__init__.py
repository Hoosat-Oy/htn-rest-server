# encoding: utf-8
import logging
import time

import aiocache
import aiohttp
from aiocache import cached

FLOOD_DETECTED = False
CACHE = None

_logger = logging.getLogger(__name__)

aiocache.logger.setLevel(logging.WARNING)


@cached(ttl=120)
async def get_htn_price():
    market_data = await get_htn_market_data()
    if market_data is None:
        raise ValueError("Market data could not be retrieved")
    return market_data.get("current_price", {}).get("usd", "Price unavailable")


@cached(ttl=300)
async def get_htn_market_data():
    endpoint = "nonkyc"
    global FLOOD_DETECTED
    global CACHE
    if not FLOOD_DETECTED or time.time() - FLOOD_DETECTED > 300:
        if endpoint == "coingecko":
            _logger.debug("Querying CoinGecko now.")
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.coingecko.com/api/v3/coins/hoosat-network", timeout=10) as resp:
                    if resp.status == 200:
                        FLOOD_DETECTED = False
                        CACHE = (await resp.json())["market_data"]
                        return CACHE
                    elif resp.status == 429:
                        FLOOD_DETECTED = time.time()
                        if CACHE:
                            _logger.warning('Using cached value. 429 detected.')
                        _logger.warning("Rate limit exceeded.")
                    else:
                        _logger.error(f"Did not retrieve the market data. Status code {resp.status}")
        elif endpoint == "nonkyc":
            _logger.debug("Querying NonKYC now.")
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.nonkyc.io/api/v2/ticker/HTN%2FUSDT", timeout=10) as resp:
                    if resp.status == 200:
                        FLOOD_DETECTED = False
                        data = (await resp.json())
                        _logger.info(data)
                        CACHE = {'usd': float(data['last_price'])}
                        return CACHE
                    elif resp.status == 429:
                        FLOOD_DETECTED = time.time()
                        if CACHE:
                            _logger.warning('Using cached value. 429 detected.')
                        _logger.warning("Rate limit exceeded.")
                    else:
                        _logger.error(f"Did not retrieve the market data. Status code {resp.status}")

    return CACHE
