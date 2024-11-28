import asyncio
import json

import websockets

from clients.ws_client import WebSocketClient
from events.event_abc import EventAbc


class WebSocketEvent(EventAbc):
    def __init__(self, client: WebSocketClient):
        """
        Initialize the WebSocketEvent handler with a WebSocket client.

        Args:
            client (WebSocketClient): The WebSocket client for communication.
        """
        self.__client = client
        self._listen_task = None

    async def __send_message(self, message: dict) -> dict:
        """
        Send a message to the WebSocket server and receive a response.

        Args:
            message (dict): The message to send.

        Returns:
            dict: The server's response.
        """
        if not self.__client.websocket:
            await self.__client.connect()
        print(f"Sending message: {message}")
        await self.__client.websocket.send(json.dumps(message))
        response = await self.__client.websocket.recv()
        print(f"Received response: {response}")
        return json.loads(response)

    async def __listen_for_messages(self):
        """
        Continuously listen for incoming messages from the WebSocket server.
        """
        print("Started listening for incoming messages...")
        try:
            async for message in self.__client.websocket:
                await self.__handle_message(message)
        except websockets.ConnectionClosed:
            print("WebSocket connection closed during message listening.")
        except Exception as e:
            print(f"Error while listening to WebSocket messages: {e}")

    async def __handle_message(self, message: str):
        """
        Process an incoming message from the WebSocket server.

        Args:
            message (str): The incoming WebSocket message.
        """
        print(f"Incoming message: {message}")
        try:
            data = json.loads(message)
            event_type = data.get("event")

            if event_type == "init_ack":
                print("Initialization acknowledged by server.")
            elif event_type == "query_result":
                print(f"Query result received: {data}")
            elif event_type == "store_result":
                print(f"Store result received: {data}")
            else:
                print(f"Unknown event received: {data}")
        except json.JSONDecodeError:
            print(f"Invalid JSON message received: {message}")

    async def on_close(self):
        """
        Handle the WebSocket close event.
        """
        print("Closing WebSocket connection...")
        await self.__client.close()
        if self._listen_task:
            self._listen_task.cancel()
        print("WebSocket connection closed.")

    async def on_init(self):
        """
        Handle the initialization event.
        Establish connection and start listening for messages.
        """
        print("Initializing WebSocket connection...")
        await self.__client.connect()
        self._listen_task = asyncio.create_task(self.__listen_for_messages())
        init_message = {"event": "init", "data": "Initialization data"}
        await self.__send_message(init_message)

    async def on_query(self):
        """
        Handle the query event.
        Send a query to the WebSocket server and process the response.
        """
        print("Sending query to WebSocket server...")
        query_message = {"event": "query", "data": {"key": "value"}}
        response = await self.__send_message(query_message)
        print(f"Query response: {response}")

    async def on_store(self):
        """
        Handle the store event.
        Send data to store to the WebSocket server.
        """
        print("Storing data to WebSocket server...")
        store_message = {"event": "store", "data": {"key": "value", "content": "example"}}
        response = await self.__send_message(store_message)
        print(f"Store response: {response}")
