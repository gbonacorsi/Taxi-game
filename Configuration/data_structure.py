from Components.objects import *
from Components.subject import *
from Components.maze_components import *
from enum import Enum

class entity_type(Enum):
    player = "player"
    client = "client"
    destination = "destination"
    wall = "wall"
    shelf = "shelf"

class components(Enum):
    Player = Player
    Client = Client
    Destination = Destination
    Wall = Wall
    Shelf = Shelf
    

class FieldRecord:
    def __init__(self, id: int, type: entity_type, instance: components, position: tuple[int, int]) -> None:
        self.id = id
        self.type = type
        self.instance = instance
        self.position = position
    
    def get_values(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "instance": self.instance,
            "position": self.position}
    
    def update_values(self, new_values: dict) -> None:
        for key, value in new_values.items():
            if hasattr(self, key):
                setattr(self, key, value)