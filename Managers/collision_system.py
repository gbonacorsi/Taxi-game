from Configuration.data_structure import entity_type
from Utils.matrix_system import Matrix

def is_collision(new_position: tuple[float, float], matrix: Matrix) -> bool:
    
    collision = False
    
    if matrix.contain_type(new_position, entity_type.wall) or matrix.contain_type(new_position, entity_type.player):
            collision = True

    return collision

def is_valide_movement(new_coordinate: tuple[float, float], matrix: Matrix) -> bool:
    
    valide_movement= not is_collision(new_coordinate, matrix)
    return valide_movement
