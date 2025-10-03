from Entities.subject import ClientEntity, PlayerEntity
from Configuration.setup import PLAYER_CAPACITY, PLAYER_DEFAULT_CAPACITY, CLIENT_VOLUME, CLIENT_DEFAULT_VOLUME

class Client(ClientEntity):
    def __init__(self, entity_id, position: tuple[ int, int], client_volume: dict = CLIENT_VOLUME[CLIENT_DEFAULT_VOLUME]):
        super().__init__(entity_id=entity_id)
        self.position=position
        self.client_volume = client_volume
        self.loaded = False
        
    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_volume(self) -> dict:
        return self.client_volume
    
    def load(self) -> None:
        self.loaded = True
    
    def unload(self) -> None:
        self.loaded = False

class Player(PlayerEntity):
    def __init__(self, entity_id:int, position: tuple[ int, int], max_clients_capacity: dict = PLAYER_CAPACITY[PLAYER_DEFAULT_CAPACITY]):
        super().__init__(entity_id=entity_id)
        self.position=position
        self.clients_loaded = []
        self.max_player_capacity = max_clients_capacity
    
    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_client_loaded(self) -> list[Client]:
        return self.clients_loaded
    
    def get_max_capacity(self) -> dict:
        return self.max_player_capacity
    
    def store_client(self, client: Client) -> None:
        self.clients = []
    
    def max_capacity(self) -> int:
        return 1
    
    def pick(self, client: Client) -> None:
        client.load()
    
    def drop(self, client: Client) -> None:
        if client in self.clients_loaded:
            self.clients_loaded.remove(client)
            client.unload()
