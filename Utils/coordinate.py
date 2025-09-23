from random import randint
from Asset.levels import maps
from Configuration.setup import MAP_INDEX
from Core.Engine import matrix

def choose_random_position(map_id=MAP_INDEX) -> tuple[float, float]:

    y = randint(0, len(maps[map_id]) - 1)
    x = randint(0, len(maps[map_id][y]) - 1)
    return (x, y)

def contain_value_with_type(coordinate: tuple[float, float], entity_type: str) -> int:

    is_found = False
    
    coordinates_value = matrix[coordinate[1]][coordinate[0]]
    for i, value in enumerate(coordinates_value):
        if value.type == entity_type:
            is_found = True
    
    return is_found
    
    
    
    
