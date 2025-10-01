from Configuration.data_structure import ComponentRecord, entity_type
from Components.subject import Player
from Managers.world_manager import World
from Managers.collision_system import is_valide_movement


def move(world: World, component: ComponentRecord ,
         current_position: tuple[float, float],
         new_position: tuple[float, float]) -> None:

    moved = False
    if is_valide_movement(new_position, world.matrix) == True:
            world.matrix.move_record(current_position, new_position, component)
            moved = True
    
    return moved

class Movement2D:

    def __init__(self, world: World, component: ComponentRecord) -> None:

        self.world = world
        self.component = component
        self.current_position = self.component.get_values()["instance"].get_position()

    def go_up(self) -> tuple[float, float]:

        new_coor = (self.current_position[0], self.current_position[1] - 1)
        moved = move(self.world,self.component, self.current_position, new_coor)      
        return self.current_position, new_coor, moved

    def go_down(self) -> tuple[float, float]:

        new_coor = (self.current_position[0], self.current_position[1] + 1)
        moved = move(self.world,self.component, self.current_position, new_coor)      
        return self.current_position, new_coor, moved

    def go_left(self) -> tuple[float, float]:
        new_coor = (self.current_position[0] - 1, self.current_position[1])
        moved = move(self.world, self.component, self.current_position, new_coor)
        return self.current_position, new_coor, moved

    def go_right(self) -> tuple[float, float]:
        new_coor = (self.current_position[0] + 1, self.current_position[1])
        moved = move(self.world, self.component, self.current_position, new_coor)
        return self.current_position, new_coor, moved