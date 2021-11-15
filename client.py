import requests
import time
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get('http://127.0.0.1:5000/currentTime') as response:
                print(response.text)
                await asyncio.sleep(1)


# Python 3.7+
asyncio.run(main())
