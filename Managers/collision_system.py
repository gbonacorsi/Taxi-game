
from Configuration.data_structure import *

def is_collision(new_coordinate: tuple[float, float], matrix: list | None) -> bool:
    
    collision = False
    
    if matrix is not None:
        
        components_found = matrix[new_coordinate(1), new_coordinate(0)]

        for component in components_found:
            if component.get_value()["type"] == entity_type.wall or component.get_value()["type"] == entity_type.player:
                collision = True
                return collision
    
    return collision

def is_valide_movement(new_coordinate: tuple[float, float]) -> bool:
    
    valide_movement=is_collision(new_coordinate)
    return valide_movement
