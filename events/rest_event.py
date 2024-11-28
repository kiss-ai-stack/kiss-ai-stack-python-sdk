from clients.rest_client import RestClient
from events.event_abc import EventAbc


class RestEvent(EventAbc):

    def __init__(self, client: RestClient):
        self.__client = client

    async def on_auth(self):
        pass

    async def on_close(self):
        await self.__client.post(
            url=f'/sessions?action=close',
            headers={},
            params={},
            request_body={}
        )

    async def on_init(self):
        await self.__client.post(
            url=f'/sessions?action=init',
            headers={},
            params={},
            request_body={}
        )

    async def on_query(self):
        await self.__client.post(
            url=f'/queries',
            headers={},
            params={},
            request_body={}
        )

    async def on_store(self):
        await self.__client.post(
            url=f'/documents',
            headers={},
            params={},
            request_body={}
        )
