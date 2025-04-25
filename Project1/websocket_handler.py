import websockets
import json
import asyncio
from Project1.py.currency import get_currency_for_last_days

async def handle_exchange_command(websocket, path):
    message = await websocket.recv()
    if message.startswith("exchange"):
        days = int(message.split()[1]) if len(message.split()) > 1 else 1
        data = await get_currency_for_last_days(days)
        await websocket.send(json.dumps(data))

async def main():
    async with websockets.serve(handle_exchange_command, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
