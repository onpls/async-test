import aiohttp
import asyncio
import time

N_ASYNC_CALLS = 10


async def api_call(mode: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"http://localhost:8000/sleepAndReturn{mode}"
        ) as response:
            await response.text()


async def main(mode: str):
    s = time.time()

    tasks = [
        asyncio.create_task(api_call(mode))
        for _ in range(N_ASYNC_CALLS)
    ]
    await asyncio.gather(*tasks)

    e = time.time()
    print(f"{mode} took {e - s}s")


if __name__ == "__main__":
    for mode in ["Async", "Sync"]:
        asyncio.run(main(mode))
