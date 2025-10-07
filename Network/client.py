import asyncio
import websockets

class ClientGame:
    def __init__(self):
        self.uri = "ws://localhost:8765"
        self.key = None
        
    async def ask_client_key(self):


        """   async def call_action(self):
        async with websockets.connect(self.uri) as websocket:
            action = input("Enter action (1: up, 2: down, 3: left, 4: right): ")
            await websocket.send(action)
            print(f"Action sent: {action}")
            response = await websocket.recv()
            print(f"Received from server: {response}")
    
    async def main(self):
        while True:
            await self.call_action()
            """
 

client=ClientGame()
asyncio.run(client.main())