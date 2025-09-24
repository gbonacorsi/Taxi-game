from Components.objects import *
from Components.subject import *
from Components.maze_components import *
from Presentation.Turtle.render_system import PlayerDisplay, ClientDisplay, DestinationDisplay, WallDisplay, ShelfDisplay
from enum import Enum

class entity_type(Enum):
    player = "player"
    client = "client"
    destination = "destination"
    wall = "wall"
    shelf = "shelf"

class displays(Enum):
    Player = PlayerDisplay
    Client = ClientDisplay
    Destination = DestinationDisplay
    Wall = WallDisplay
    Shelf = ShelfDisplay

class components(Enum):
    Player = Player
    Client = Client
    Destination = Destination
    Wall = Wall
    Shelf = Shelf

class lang(Enum):
    eng = "English"
    
class actions(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    pick = "pick"
    drop = "drop"

class FieldRecord:
    def __init__(self, id: int, type: entity_type, instance: components, position: tuple[int, int], grid_id: int | None = None) -> None:
        self.id = id
        self.type = type
        self.instance = instance
        self.position = position
        self.grid_id = grid_id

    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
            "position": self.position,
            "grid_id": self.grid_id
        }

    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)

class FieldDisplay:
    def __init__(self, id: int, type: entity_type, instance: displays, position: tuple[int, int]) -> None:
        self.id = id
        self.type = type
        self.instance = instance
        self.position = position

    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
            "position": self.position,
        }

    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)