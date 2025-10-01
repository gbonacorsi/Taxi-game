from Entities.maze_structure import WallEntity, ShelfEntity

class Wall(WallEntity):
    def __init__(self, entity_id:int, position = tuple[int, int]):
        super().__init__(entity_id=entity_id)
        self.position = position
    
    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position

class Shelf(ShelfEntity):
    def __init__(self, entity_id:int, position = tuple[int, int]):
        super().__init__(entity_id=entity_id)
        self.position = position

    def set_position(self,position: tuple[ int, int]) -> None:
        self.position = position

    def get_position(self) -> tuple[int, int]:
        return self.position
    
