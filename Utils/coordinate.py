from random import randint
from Asset.levels import maps

def which_entity_is_it(x: float, y: float, map_id: int) -> dict[int: str]:

    """Check if the given coordinates correspond to a shelf in the specified map.
    
    Args:
        x: X coordinate to check.
        y: Y coordinate to check.
        map_id: ID of the map to check against.

    Returns:
        dict[int: str]: A dictionary with the entity type if found, otherwise an empty dictionary.
            {0: "shelf"}, {1: "wall"}, {2: "player"}, {3: "client"}, {4: "destination"}, {5: "empty"}
    """
    
    if maps[map_id][y][x] == "#":
        return {0: "shelf"}
    elif maps[map_id][y][x] == "!":
        return {1: "wall"}
    elif maps[map_id][y][x] == "P":
        return {2: "player"}
    elif maps[map_id][y][x] == "c":
        return {3: "client"}
    elif maps[map_id][y][x] == "X":
        return {4: "destination"}
    else:
        return {5: "empty"}

def choose_random_position(map_id) -> tuple[float, float]:
    
    """Choose a random position on the map
    
    Args:
        map_id: ID of the map to choose the position from.
    
    Returns:
        tuple[float, float]: A tuple containing the (x, y) coordinates of the chosen position.
    """
    
    y = randint(0, len(maps[map_id]) - 1)
    x = randint(0, len(maps[map_id][y]) - 1)
    return (x, y)