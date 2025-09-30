from Entities.subject import ClientEntity, PlayerEntity

class Client(ClientEntity):
    def __init__(self, entity_id, position: tuple[ int, int]):
        super().__init__(entity_id=entity_id)
        self.position=position
        self.loaded = False
        
    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def load(self) -> None:
        self.loaded = True
    
    def unload(self) -> None:
        self.loaded = False

class Player(PlayerEntity):
    def __init__(self, entity_id:int, position: tuple[ int, int]):
        super().__init__(entity_id=entity_id)
        self.position=position
        self.picked_client = False
    
    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def picked(self) -> None:
        self.picked_client = True

    def dropped(self) -> None:
        self.picked_client = False