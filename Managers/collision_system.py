from Configuration.data_structure import entity_type
from Utils.matrix_system import Matrix

def is_collision(new_position: tuple[float, float], matrix: Matrix) -> bool:
    
    is_collision = []
    
    if matrix.contain_type(new_position, entity_type.wall):
        is_collision.append(entity_type.wall)
    if matrix.contain_type(new_position, entity_type.player):
        is_collision.append(entity_type.player)
    if matrix.contain_type(new_position, entity_type.shelf):
        is_collision.append(entity_type.shelf)
    if matrix.contain_type(new_position, entity_type.client):
        is_collision.append(entity_type.client)
    if matrix.contain_type(new_position, entity_type.destination):
        is_collision.append(entity_type.destination)

    return is_collision
