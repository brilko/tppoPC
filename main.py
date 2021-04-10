import asyncio
import websockets

client = None

async def echo(websocket, path):
    client = websocket
    async for message in websocket:
        print(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '', 8080))
asyncio.get_event_loop().run_forever()

async def sendScreenRatio(screenRatio):
    if (client):
        await client.send(screenRatio)