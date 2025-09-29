
from Configuration.data_structure import *
from Managers.world_manager import World
from Managers.collision_system import is_valide_movement

def move(world: World | None = None,field: FieldRecord | None = None, 
         new_coor: tuple[float, float] | None = None, current_position: tuple[float, float] | None = None) -> None:
    
    if is_valide_movement(new_coor, world.matrix) == True:
        print(world.map)
        field = world.matrix[current_position[0]][current_position[1]]
        #field.update_values({"position": new_coor})
        
        world.add_component(new_coor, field)
        world.remove_component(current_position, field)
        
        print(world.map)

class Movement2D:

    def __init__(self, world: World | None = None, field: FieldRecord | None = None) -> None:

        self.world = world
        self.field =field
        self.current_position = self.field.get_values()["position"]

    def go_up(self) -> tuple[float, float]:

        new_coor = (self.current_position[0], self.current_position[1] - 1)
        move(self.world, self.field, new_coor, self.current_position)

    def go_down(self) -> tuple[float, float]:

        new_coor = (self.current_position[0], self.current_position[1] + 1)
        move(self.world, self.field, new_coor, self.current_position)

    def go_left(self) -> tuple[float, float]:
        new_coor = (self.current_position[0] - 1, self.current_position[1])
        move(self.world, self.field, new_coor, self.current_position)

    def go_right(self) -> tuple[float, float]:
        new_coor = (self.current_position[0] + 1, self.current_position[1])
        move(self.world, self.field, new_coor, self.current_position)