from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

from kiss_ai_stack_types.models import GenericResponseBody, SessionResponse

class EventAbc(ABC):
    """
    Abstract Base Class for defining the structure of event-based operations
    for an AI agent. These operations include authorization, lifecycle
    management, and data handling.
    """

    @abstractmethod
    async def authorize_agent(self, client_id: Optional[str] = None, client_secret: Optional[str] = None,
                              scope: Optional[str] = None) -> SessionResponse:
        """
        Authorizes the agent using provided credentials and scope. If you have saved a previous client_id and
        a client_secret send them to get a new access token. Only `persistent` scope supports this. `temporary`
        scope will deactivate the client upon lifecycle ending. Only send the `scope` to generate a new client
        and keep it saved for `persistent` sessions.

        :param client_id: (Optional[str]): The client ID for the agent.
        :param client_secret: (Optional[str]): The client secret for authentication.
        :param scope: (Optional[str]): The scope of the authorization.

        :returns SessionResponse: The response containing session details.
            - client_id
            - client_secret
            - scope
        """
        pass

    @abstractmethod
    async def destroy_agent(self, data: Optional[str] = None) -> GenericResponseBody:
        """
        Destroys the agent and cleans up any associated resources.

        :params data: (Optional[str]): Preferably a goodbye message.
        :returns: GenericResponseBody: The response indicating the success or failure of the operation.
        """
        pass

    @abstractmethod
    async def bootstrap_agent(self, data: Optional[str] = None) -> GenericResponseBody:
        """
        Bootstraps the agent session in server by initializing necessary components and configurations.

        :param data: (Optional[str]): Preferably a greeting message.
        :returns GenericResponseBody: The response indicating the success or failure of the operation.
        """
        pass

    @abstractmethod
    async def generate_answer(self, data: Optional[str]) -> GenericResponseBody:
        """
        Generates an answer based on the provided query or prompt.

        :param data: (Optional[str]): Input query/prompt used to generate the answer.
        :returns GenericResponseBody: The response containing the generated answer.
        """
        pass

    @abstractmethod
    async def store_data(self, files: List[str], metadata: Optional[Dict[str, Any]] = None) -> GenericResponseBody:
        """
        Stores files as documents, only rag based tools are supported.

        :param files: (List[str]): A list of file paths to be stored.
        :param metadata: (Optional[Dict[str, Any]]): Additional metadata associated with the files.
        :returns GenericResponseBody: The response indicating the success or failure of the operation.
        """
        pass
