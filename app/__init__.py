import asyncio
import time
import os

from fastapi import FastAPI

app = FastAPI()

SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 2))


@app.get("/sleepAndReturnAsync")
async def sleepAndReturnAsync():
    await asyncio.sleep(SLEEP_TIME)  # Detachable
    return f"Slept for {SLEEP_TIME} s."


@app.get("/sleepAndReturnSync")
async def sleepAndReturnSync():
    time.sleep(SLEEP_TIME)  # Blocking
    return f"Slept for {SLEEP_TIME} s."
