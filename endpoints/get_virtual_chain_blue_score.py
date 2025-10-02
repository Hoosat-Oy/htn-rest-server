# encoding: utf-8
import asyncio
from pydantic import BaseModel

from server import app, htnd_client

current_blue_score_data = {
    "blue_score": 0
}


class BlockdagResponse(BaseModel):
    blueScore: int = 260890


@app.get("/info/virtual-chain-blue-score", response_model=BlockdagResponse, tags=["Hoosat network info"])
async def get_virtual_selected_parent_blue_score():
    """
    Returns the blue score of virtual selected parent
    """
    resp = await htnd_client.request("getVirtualSelectedParentBlueScoreRequest")
    return resp["getVirtualSelectedParentBlueScoreResponse"]


async def update_blue_score():
    global current_blue_score_data
    while True:
        try:
            resp = await htnd_client.request("getVirtualSelectedParentBlueScoreRequest")
            current_blue_score_data["blue_score"] = int(resp["getVirtualSelectedParentBlueScoreResponse"]["blueScore"])
        except Exception as e:
            # Log error but continue the loop
            pass
        await asyncio.sleep(5)