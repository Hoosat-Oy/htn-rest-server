# encoding: utf-8
import logging
import os

import fastapi.logger
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_utils.tasks import repeat_every
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from h11._util import LocalProtocolError, RemoteProtocolError

from helper.LimitUploadSize import LimitUploadSize
from htnd.HtndMultiClient import HtndMultiClient

fastapi.logger.logger.setLevel(logging.WARNING)

app = FastAPI(
    title="Hoosat REST-API server",
    description="This server is to communicate with Hoosat Network via REST-API",
    version=os.getenv("VERSION", "tbd"),
    contact={
        "name": "lAmeR1"
    },
    license_info={
        "name": "MIT LICENSE"
    }
)

app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_middleware(LimitUploadSize, max_upload_size=200_000)  # ~1MB

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PingResponse(BaseModel):
    serverVersion: str = "0.12.2"
    isUtxoIndexed: bool = True
    isSynced: bool = True



class H11ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except (LocalProtocolError, RemoteProtocolError) as exc:
            logging.warning(f"Caught h11 protocol error: {exc}")
            return JSONResponse(
                status_code=400,
                content={"message": "Invalid HTTP request received"}
            )

app.add_middleware(H11ErrorMiddleware)


@app.get("/ping",
         include_in_schema=False,
         response_model=PingResponse)
async def ping_server():
    """
    Ping Pong
    """
    try:
        info = await htnd_client.htnds[0].request("getInfoRequest")
        if not info or not info.get("getInfoResponse"):
            raise HTTPException(status_code=500, detail="Invalid response from htnd.")
        assert info["getInfoResponse"]["isSynced"] is True

        return {
            "server_version": info["getInfoResponse"]["serverVersion"],
            "is_utxo_indexed": info["getInfoResponse"]["isUtxoIndexed"],
            "is_synced": info["getInfoResponse"]["isSynced"]
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail="htnd not connected.")


htnd_hosts = []

for i in range(100):
    try:
        htnd_hosts.append(os.environ[f"HTND_HOSTS_{i + 1}"].strip())
    except KeyError:
        break

if not htnd_hosts:
    raise Exception('Please set at least HTND_HOSTS_1 environment variable.')

htnd_client = HtndMultiClient(htnd_hosts)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    await htnd_client.initialize_all()
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"
                 # "traceback": f"{traceback.format_exception(exc)}"
                 },
    )


@app.on_event("startup")
@repeat_every(seconds=60)
async def periodical_blockdag():
    await htnd_client.initialize_all()
