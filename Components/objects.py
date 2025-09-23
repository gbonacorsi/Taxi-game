from Entities.objects import *

class Destination(DestinationEntity):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.arrived = False
        super().__init__()

    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y
        return (self.x, self.y)
    
    def get_position(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def set_arrived(self) -> None:
        self.arrived = True
    
    def clear_arrival(self) -> None:
        self.arrived = False