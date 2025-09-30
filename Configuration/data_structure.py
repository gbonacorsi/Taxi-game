from enum import Enum
from turtle import position
from Components.objects import Destination
from Components.subject import Player, Client
from Components.maze_components import Wall, Shelf
from Presentation.Turtle.components_display import PlayerDisplay, ClientDisplay, DestinationDisplay, WallDisplay, ShelfDisplay

# Note: 
#   Accross the project the position is a tuple (x, y). You will find often express like position: tuple[int, int]

class actions(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    pick = "pick"
    drop = "drop"
    
class components(Enum):
    Player = Player
    Shelf = Shelf
    Wall = Wall
    Client = Client
    Destination = Destination
    
class displays(Enum):
    Player = PlayerDisplay
    Client = ClientDisplay
    Destination = DestinationDisplay
    Wall = WallDisplay
    Shelf = ShelfDisplay
    
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
    def __init__(self, id: int, type: entity_type, instance: components, position = tuple[int, int]) -> None:
        self.id = id
        self.type = type
        self.instance = instance
        self.position = position

    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
            "position": self.position
        }

    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)

class DisplayRecord:
    def __init__(self, id: int, type: entity_type, instance: displays, blink_state: bool = False) -> None:
        self.id = id
        self.type = type
        self.instance = instance
        self.blink_state = blink_state

    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
            "blink_state": self.blink_state,
        }

    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)

