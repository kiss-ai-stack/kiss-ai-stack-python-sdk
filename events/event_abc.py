from abc import ABC, abstractmethod


class EventAbc(ABC):

    @abstractmethod
    async def on_close(self):
        pass

    @abstractmethod
    async def on_init(self):
        pass

    @abstractmethod
    async def on_query(self):
        pass

    @abstractmethod
    async def on_store(self):
        pass
