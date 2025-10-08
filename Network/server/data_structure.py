from enum import Enum
import secrets
import string
import json
from Configuration.data_structure import actions


communication_actions = {
    0: actions.wait,
    1: actions.up,
    2: actions.down,
    3: actions.left,
    4: actions.right,
    5: actions.pick,
    6: actions.drop
}

communication_status = {
    # Success
    200: "OK",
    201: "CREATED", 
    202: "ACCEPTED",
    204: "NO_CONTENT",
    
    # Client Errors
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
    409: "CONFLICT",
    422: "UNPROCESSABLE_ENTITY",
    429: "TOO_MANY_REQUESTS",
    
    # Server Errors
    500: "INTERNAL_SERVER_ERROR",
    501: "NOT_IMPLEMENTED",
    503: "SERVICE_UNAVAILABLE",
    504: "GATEWAY_TIMEOUT"
}

class request_type(Enum):
    request_key = "request_key"
    confirm_key = "confirm_key"
    action = "action"
    
def generate_auth_key(length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for _ in range(length))

    return key

def generate_session_id(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for _ in range(length))

    return key

class CommunicationData:
    
    def __init__(self, 
                 auth_key: str = None, 
                 session_id: str = None, 
                 request_type: str = None,
                 message_status: int = 0, 
                 action_number: int = 0,
                 new_observation: str = None,
                 reward: str = None,
                 terminated: bool = False,
                 truncated: bool = False,
                 information: str = None) -> None:

        self.auth_key = auth_key
        self.session_id = session_id
        self.request_type = request_type
        self.message_status = message_status
        self.action_number = action_number
        self.new_observation = new_observation
        self.reward = reward
        self.terminated = terminated
        self.truncated = truncated
        self.information = information

    def get_values(self) -> dict:
        return {
            "header": {
                "auth_key": self.auth_key if self.auth_key is not None else "",
                "session_id": self.session_id if self.session_id is not None else "",
                "request_type": self.request_type if self.request_type is not None else "",
                "message_status": self.message_status if self.message_status != 0 else 0,
            },
            "body": {
                "action_number": self.action_number if self.action_number != 0 else 0,
                "new_observation": self.new_observation if self.new_observation is not None else "",
                "reward": self.reward if self.reward is not None else "",
                "terminated": self.terminated if self.terminated is not None else "",
                "truncated": self.truncated if self.truncated is not None else "",
                "information": self.information if self.information is not None else "",
            }
        }
    
    def get_json(self) -> str:
        data = self.get_values()
        return json.dumps(data)
    
    def read_json(self, json_string: str) -> None:
        try:
            data = json.loads(json_string)
            self.create(data)
            return True
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return False

    def is_action_valid(self, action: str):
        try:
            if action is not None:
                action_number = int(action)
                communication_actions[action_number]
                return True
        except KeyError:
            return False

    def is_request_key_valid(self, request_key: str):
        try:
            request_key = str(request_key)
            request_type[request_key]
            return True
        except KeyError:
            return False
    
    def is_valid_status(self, status_code: int) -> bool:
        try:
            if status_code is not None:
                status_value = int(status_code)
                communication_status[status_value]
                return True
        except KeyError:
            return False
    
    def create(self, data: dict) -> None:
        
        contain_header = "header" in data
        contain_body = "body" in data

        header = data["header"] if contain_header else {}
        body = data["body"] if contain_body else {}

        if contain_header:
            self.auth_key = header["auth_key"] if "auth_key" in header else None
            self.session_id = header["session_id"] if "session_id" in header else None
            self.request_type = header["request_type"] if "request_type" in header and self.is_request_key_valid(header["request_type"]) else None
            self.message_status = header["message_status"] if self.is_valid_status(header["message_status"]) else None

        if contain_body:
            self.action_number = body["action_number"] if "action_number" in body and self.is_action_valid(body["action_number"]) else None
            self.new_observation = body["new_observation"] if "new_observation" in body else None
            self.reward = body["reward"] if "reward" in body else None
            self.terminated = body["terminated"] if "terminated" in body else None
            self.truncated = body["truncated"] if "truncated" in body else None
            self.information = body["information"] if "information" in body else None



