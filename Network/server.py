import asyncio
import websockets
from Core.game_manager import GameManager
from Network.data_structure import CommunicationData, request_type, comunication_status, data_model
from Configuration.setup import PLAYERS_NUMBER,

class GameServer:

    def __init__(self, game_manager: GameManager) -> None:
        self.game_manager = game_manager
        self.session_id = 0
        self.auth_key_list = []

    async def attribution_key(self, session_id, websocket):

        key_number = len(self.auth_key_list)
        
        if key_number < PLAYERS_NUMBER:
            clients_components = self.game_manager.world.clients[key_number]
            new_key = CommunicationData().generate_auth_key()
            record = (clients_components, new_key)
            self.auth_key_list.append(record)
            print("Client connected, generating auth key...")

            message_201 = CommunicationData(
                auth_key=new_key,
                session_id=session_id,
                request_type=request_type.request_key.value,
                status=201
            )

            message_201 = CommunicationData()

            await websocket.send(message_201.get_json())
            print(f"Client associated and auth key allocated: {new_key}")

        else:
            
            message_501 = CommunicationData(
                auth_key=new_key,
                session_id=session_id,
                request_type=request_type.request_key.v
                alue,
                status=501
            )

            await websocket.send(message_501.get_json())
            print(f"Client associated and auth key allocated: {new_key}")
        

    async def listenner(self, websocket):
        print("Server started, waiting for messages...")
        message = await websocket.recv()

        data = CommunicationData()
        result = data.read_json(message)

        if result:
            print("Message processed successfully.")
            if data.request_type== request_type.request_key.value:
                await self.attribution_key(data.session_id, websocket)
        else:
            print("Failed to process message.")

    """
    async def action(self, websocket):
        print("Server started, waiting for actions...")
        message = await websocket.recv()
        print(f"Message received: {message}")

        is_valid_action, action_enum = is_action_valid(int(message))

        if is_valid_action:
            print(f"Action received: {action_enum.value}")
            self.game_manager.action(action_enum)
            await websocket.send(f"Action {action_enum.value} executed")
            
        else:
            print(f"Invalid action")
    """
    
    async def main(self):
        self.session_id += 1
        async with websockets.serve(self.listenner, "localhost", 8765):
            await asyncio.Future() 
            
    def run(self):
        asyncio.run(self.main())

