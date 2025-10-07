from enum import Enum
from turtle import position
from Components.objects import Destination
from Components.subject import Player, Client
from Components.maze_components import Wall, Shelf
from Presentation.Turtle.components_display import PlayerDisplay, ClientDisplay, DestinationDisplay, WallDisplay, ShelfDisplay
from Utils.exeption_system import ActionError

# Note: 
#   Accross the project the position is a tuple (x, y). You will find often express like position: tuple[int, int]

class actions(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    pick = "pick"
    drop = "drop"

def is_valid_action_name(action_name: str) -> bool:
    try:
        _ = actions[action_name.lower()]
        return True
    except ActionError:
        return False

class component_record_keys(Enum):
    id = "id"
    type = "type"
    instance = "instance"
    position = "position"

class display_record_keys(Enum):
    id = "id"
    type = "type"
    instance = "instance"
    blink_state = "blink_state"
    
class entity_type(Enum):
    player = "player"
    client = "client"
    destination = "destination"
    wall = "wall"
    shelf = "shelf"
    
class ComponentRecord:
    def __init__(self, id: int, type: entity_type, instance: None | Destination | Player | Client | Wall | Shelf) -> None:
        self.id = id
        self.type = type
        self.instance = instance

    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
        }

    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)


