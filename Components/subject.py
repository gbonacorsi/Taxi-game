from Entities.subject import *

class Client(ClientEntity):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.loaded = False
        super().__init__()
        
    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y
        return (self.x, self.y)
    
    def get_position(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def set_load(self) -> None:
        self.loaded = True
    
    def set_unload(self) -> None:
        self.loaded = False

class Player(PlayerEntity):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.picked_client = False
        super().__init__()
    
    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y
        return (self.x, self.y)
    
    def get_position(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def set_picked(self) -> None:
        self.picked_client = True

    def set_dropped(self) -> None:
        self.picked_client = False