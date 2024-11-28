import websockets


class WebSocketClient:
    def __init__(self, ws_url: str):
        self.ws_url = ws_url
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(self.ws_url)

    async def close(self):
        if self.websocket:
            await self.websocket.close()
