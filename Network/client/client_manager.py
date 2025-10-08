import asyncio
import websockets
from data_structure import CommunicationData, request_type


class ClientGame:
    def __init__(self):
        self.uri = "ws://localhost:8765"
        self.session_id = None
        self.key = None

    async def send_message_and_wait_feedback(self, message: CommunicationData, websocket):
        
        await websocket.send(message.get_json())
        response_data = await websocket.recv()
        response = CommunicationData()
        response.read_json(response_data)

        status = response.message_status

        if status == 200:
            print("Feedback successfully received from server.")
        if status == 201:
            print("Creation confirmed from server.")
        if status == 501:
            print("Failed from server.")

        return status, response

    async def ask_client_key(self, websockets):
            
            message = CommunicationData(
                request_type=request_type.request_key.value,
            )

            feedback_status, feedback_message = await self.send_message_and_wait_feedback(message, websockets)
            print("Key request sent to server.")

            if feedback_status == 201:
                self.session_id = feedback_message.session_id
                self.key = feedback_message.auth_key
                
                message = CommunicationData(
                    session_id=self.session_id,
                    auth_key=self.key,
                    request_type=request_type.confirm_key.value,
                    message_status= 200)
                
                feedback_status, feedback_message = await self.send_message_and_wait_feedback(message, websockets)

                if feedback_status == 200:
                    print("Key successfully confirmed")
                elif feedback_status == 501:
                    print("Failed to confirmation key")

            elif feedback_status == 501:
                print("Failed to receive key: maximum clients reached.")
            
    async def call_action(self, action, websockets):
        
        message = CommunicationData(
            session_id=self.session_id,
            auth_key=self.key,
            request_type=request_type.action.value,
            action_number=int(action)
        )
        
        feedback_status, feedback_message = await self.send_message_and_wait_feedback(message, websockets)
        print("Action request sent to server.")
        
        if feedback_status == 201:
            print("Action successfully sent to server.")
        else:
            print("Failed to send action to server.")

        #print(f"New observation: {feedback_message.new_observation}, Reward: {feedback_message.reward}, Terminated: {feedback_message.terminated}")
        return feedback_message.new_observation, feedback_message.reward, feedback_message.terminated

    async def execute_action(self, action):

        if not self.session_id or not self.key:
            raise Exception
        
        async with websockets.connect(self.uri) as websocket:
            return await self.call_action(action, websocket)

    async def initialize(self):
        async with websockets.connect(self.uri) as websocket:
            await self.ask_client_key(websocket)
    

    async def main(self):
        action = input("Enter action (0: wait, 1: up, 2: down, 3: left, 4: right, 5: pick, 6: drop): ")
        await self.execute_action(action)
        await asyncio.Future() 
