import asyncio
import websockets
from Core.game_manager import GameManager
from Network.data_structure import CommunicationData, generate_session_id, request_type, communication_status, data_model, generate_auth_key
from Configuration.setup import PLAYERS_NUMBER
from Components.subject import Client


class GameServer:

    def __init__(self, game_manager: GameManager) -> None:
        self.game_manager = game_manager
        self.session_id = 0
        self.auth_key_list = []
        
        self.new_observatio: tuple[int, int] = (0, 0)
        self.reward: int = 0
        self.terminated: bool = False
        self.truncated: bool = False
        self.info: str = ""

    async def collect_feedback(self, client: Client):
        self.reward: int = self.game_manager.event_manager.scoring_system.get_score()
        
        
        
        
        

    async def attribution_key(self, session_id, websocket):

        key_number = len(self.auth_key_list)
        
        if key_number < PLAYERS_NUMBER:
            clients_components = self.game_manager.world.clients[key_number]
            new_key = generate_auth_key()
            record = (clients_components, new_key)
            self.auth_key_list.append(record)
            print("Client connected, generating auth key...")

            message_201 = CommunicationData(
                auth_key=new_key,
                session_id=self.session_id,
                request_type=request_type.request_key.value,
                status=201
            )

            await websocket.send(message_201.get_json())
            print(f"Client associated and auth key allocated: {new_key}")

        else:
            
            message_501 = CommunicationData(
                session_id=session_id,
                request_type=request_type.request_key.value,
                status=501
            )

            await websocket.send(message_501.get_json())
            print(f"Client associated key failed: max clients reached")
    
    async def action(self, websocket, data : CommunicationData):
        print(f"Message received: {data}")

        action = data.action_number

        print(f"Action received: {action}")
        self.terminated = self.game_manager.action(action)
        
        
        
        await websocket.send(f"Action {action} executed")


    async def listenner(self, websocket):
        print("Server started, waiting for messages...")
        message = await websocket.recv()

        data = CommunicationData()

        if data:
            print("Message received and processing...")
            if data.request_type== request_type.request_key.value:
                await self.attribution_key(data.session_id, websocket)
            elif data.request_type == request_type.action.value:
                await self.action(websocket, data)
        else:
            print("Failed to process message.")
    
    async def main(self):
        self.session_id = generate_session_id(10)
        print(f"Session ID: {self.session_id}")
        async with websockets.serve(self.listenner, "localhost", 8765):
            await asyncio.Future() 
            
    def run(self):
        asyncio.run(self.main())

