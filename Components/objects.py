from Entities.objects import DestinationEntity

class Destination(DestinationEntity):
    def __init__(self, entity_id:int, position: tuple[ int, int]):
        super().__init__(entity_id=entity_id)
        self.position = position
        self.arrived = False

    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_arrived_status(self) -> bool:
        return self.arrived
    
    def arrived(self) -> None:
        self.arrived = True
    
    def clear_arrival(self) -> None:
        self.arrived = False
    
    def get_observation(self) -> dict:
        return {
            "id": self.entity_id,
            "position": self.position,
            "arrived": self.arrived,
        }