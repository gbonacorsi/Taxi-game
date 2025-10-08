import asyncio
import websockets
from Core.game_manager import GameManager
from Components.subject import Client, Player
from Components.objects import Destination
from Network.server.data_structure import CommunicationData, generate_session_id, request_type, generate_auth_key, communication_actions
from Configuration.setup import PLAYERS_NUMBER


class GameServer:

    def __init__(self, game_manager: GameManager) -> None:
        self.game_manager = game_manager
        self.session_id = 0
        self.auth_key_list = []
        
        self.new_observation = None
        self.reward: int = 0
        self.terminated: bool = False
        self.truncated: bool = False
        self.info: str = ""

    async def send_message(self, message: CommunicationData, websocket):
        
        await websocket.send(message.get_json())
        response_data = await websocket.recv()
        response = CommunicationData()
        response.read_json(response_data)
        status_feedback = response.message_status
        print(f"Received from client: {response.get_json()}")
        
        if status_feedback == 200:
            print("Feedback successfully received from client.")
        if status_feedback == 201:
            print("Creation confirmed from client.")
        if status_feedback == 501:
            print("Failed from client")

        return status_feedback, response

    def collect_observation(self, auth_key: str) -> None:

        clients_components = self.game_manager.world.clients
        destinations_components = self.game_manager.world.destinations
        
        clients={}
        for client_component in clients_components:
            client : Client = client_component.instance
            client_data = client.get_observation()
            clients[client.entity_id]= client_data

        destinations={}
        for destination_component in destinations_components:
            destination : Destination = destination_component.instance
            destination_data = destination.get_observation()
            destinations[destination.entity_id]= destination_data
        
        players={}
        for record in self.auth_key_list:
            if record[0] == auth_key:
                player = record[1].instance
                player_position = player.get_observation()
                players[player.entity_id] = player_position
                break
        
        self.new_observation = {
            "player": players,
            "clients": clients,
            "destinations": destinations
        }
    
    def collect_reward(self) -> None:
        self.reward: int = self.game_manager.event_manager.scoring_system.get_score()

    async def attribution_key(self, session_id, websocket):

        key_number = len(self.auth_key_list)
        
        if key_number < PLAYERS_NUMBER:
            players_components = self.game_manager.world.players[key_number]
            new_key = generate_auth_key()
            record = (new_key, players_components)
            print("Client connected, generating auth key...")

            message_201 = CommunicationData(
                auth_key=new_key,
                session_id=self.session_id,
                request_type=request_type.request_key.value,
                message_status=201
            )

            status, feedback_message = await self.send_message(message_201, websocket)
            
            if feedback_message.request_type == request_type.confirm_key.value:
                self.auth_key_list.append(record)

                message = CommunicationData(
                    auth_key=new_key,
                    session_id=session_id,
                    request_type=request_type.confirm_key.value,
                    message_status=200
                )

                await websocket.send(message.get_json())
                print(f"Client associated and auth key allocated: {new_key}")
            
            else:
                print(f"Failed to allocate auth key: {feedback_message.get_json()}")

        else:
            
            message_501 = CommunicationData(
                session_id=session_id,
                request_type=request_type.request_key.value,
                message_status=501
            )

            await websocket.send(message_501.get_json())
            print(f"Client associated key failed: max clients reached")
    
    async def action(self, websocket, data : CommunicationData):

        action_number= data.action_number
        action_enum=communication_actions[action_number]
        
        auth_key = data.auth_key
        for record in self.auth_key_list:
            if record[0] == auth_key:
                player = record[1]
                break   
        
        self.terminated = self.game_manager.action(action_enum, player)
        
        self.collect_observation(auth_key)
        self.collect_reward()
        
        data = CommunicationData(
            auth_key=data.auth_key,
            session_id=self.session_id,
            request_type=request_type.action.value,
            message_status=201,
            new_observation=self.new_observation,
            reward=self.reward,
            terminated=self.terminated,
            #truncated=self.truncated,
            #info=self.info
        )
        
        message = data.get_json()
        print(f"Sending to client: {message}")
        await websocket.send(message)

    async def listenner(self, websocket):
        print("🔗 Client connected, starting message loop...")
        
        try:
            while True:
                message = await websocket.recv()
                print(f"Message received: {message}")
                
                data = CommunicationData()
                success = data.read_json(message)
                
                if success:
                    print(f"Message parsed successfully")
                    
                    if data.request_type == request_type.request_key.value:
                        print("Processing authentication request...")
                        await self.attribution_key(data.session_id, websocket)
                        
                    elif data.request_type == request_type.action.value:
                        print(f"Processing action...")
                        await self.action(websocket, data)
                        
                    else:
                        print(f"Unknown request type: {data.request_type}")
                    
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
        except Exception as e:
            print(f"Error in listener: {e}")
        finally:
            print("Cleaning up connection")
    
    async def main(self):
        self.session_id = generate_session_id(10)
        print(f"Session ID: {self.session_id}")
        print("Server started, waiting for messages...")
        async with websockets.serve(self.listenner, "localhost", 8765):
            await asyncio.Future() 
            
    def run(self):
        asyncio.run(self.main())

