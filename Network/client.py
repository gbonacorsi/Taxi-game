import asyncio
import websockets
from Network.data_structure import CommunicationData, request_type


class ClientGame:
    def __init__(self):
        self.uri = "ws://localhost:8765"
        self.session_id = None
        self.key = None
        self.status = None
        
    async def ask_client_key(self):
        async with websockets.connect(self.uri) as websocket:
            
            message = CommunicationData(
                request_type=request_type.request_key.value,
            )

            await websocket.send(message.get_json())
            response = await websocket.recv()
            print(f"Received from server: {response}")
            self.key = response
            
            message = message.read_json(response)
            self.status = message["header"]["status"]
            
            if self.status == 201:
                print("Key successfully received from server.")
                self.session_id = message["header"]["session_id"]
                self.key = message["header"]["auth_key"]
            if self.status == 501:
                print("Failed to receive key: maximum clients reached.")

    async def call_action(self):
        async with websockets.connect(self.uri) as websocket:
            action = input("Enter action (0: wait, 1: up, 2: down, 3: left, 4: right, 5: pick, 6: drop): ")
            
            data = CommunicationData(
                session_id=self.session_id,
                auth_key=self.key,
                request_type=request_type.action.value,
                action_number=int(action)
            )
            
            message = data.get_json()
            print(f"Sending to server: {message}")
            await websocket.send(message)
            
            response = await websocket.recv()
            print(f"Received from server: {response}")

            
    async def main(self):
        await self.ask_client_key
        
        if self.status == 201:
            await self.call_action()

    async def main(self):
        while True:
            await self.call_action()


client=ClientGame()
asyncio.run(client.main())