<div style="text-align: left; margin-bottom: 20px;">
  <img src="https://kiss-ai-stack.github.io/kissaistack.svg" alt="KISS AI Stack Banner" style="max-width: auto; height: 250px">
</div>



# KISS AI Stack - Client

The KISS AI Stack Client provides an easy-to-use interface for interacting with the KISS AI Stack Server, 
supporting RESTful and WebSocket APIs to manage Stack session lifecycle and execute tasks.

---

## Features

- REST client for session management, query execution, and document storage.
- WebSocket client for real-time interactions with the Stack.

---

## Getting Started

<span style="color: red; font-weight: bold;">Nota Bene:</span>  
_It is recommended to use this client in a proxy service for better security._

### Requirements

- Python 3.12

### Installation

1. Install the `kiss-ai-stack-client` package:
```bash
pip install kiss-ai-stack-client~=0.1.0a6
```

2. Initialize the client:

- REST API client

```python
from kiss_ai_stack_client import RestEvent

# host name without mentioning protocol, i.e. example.com, localhost:8080
# secure_protocol, whether to use https or http
client = RestEvent(hostname="your-server-hostname", secure_protocol=True)
```

- Websocket based client

```python
from kiss_ai_stack_client import WebSocketEvent

# host name without mentioning protocol, i.e. example.com, localhost:8080
# secure_protocol, whether to use wss or ws
client = WebSocketEvent(hostname="your-server-hostname", secure_protocol=True)
```
---

## Usage

### 1. Authorize a Stack Session
Create or refresh a Stack session:

To authorize the session, if you have saved a previous `client_id` and a `client_secret` send them to get a new access token. Only `persistent` scope supports this. `temporary` scope will deactivate the client upon lifecycle ending.  
Just send the `scope` only to generate a new client and keep it saved for `persistent` sessions.

```python
session = await client.authorize_stack(scope="temporary")  # scopes - 'temporary', 'persistent'

# or, get a new access token for a previous 'persistent session'
session = await client.authorize_stack(client_id="your-client-id", client_secret="your-client-secret")
```

### 2. Bootstrap the Stack
Initialize the Stack session for task execution:

This step is a **must** to start the Stack session.

```python
response = await client.bootstrap_stack(data="Hello, Stack!")
```

### 3. Generate an Answer
Send a query and receive the Stack's response:

```python
response = await client.generate_answer(data="What is the weather today?")
```

### 4. Store Documents
Upload files with optional metadata for storage:

```python
files = ["path/to/document1.txt", "path/to/document2.pdf"]
metadata = {"category": "example"}
response = await client.store_data(files=files, metadata=metadata)
response = await client.generate_answer(data='Give me a summary of example documents')
```

### 5. Destroy the Stack Session
Close the current session(will clean up stored documents in temporary session if it has):

```python
response = await client.destroy_stack(data="Goodbye!")
```

---

## License

This project is licensed under the MIT License.
