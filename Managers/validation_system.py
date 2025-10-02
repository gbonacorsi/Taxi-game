from Configuration.data_structure import entity_type
from Utils.matrix_system import Matrix
from Managers.collision_system import is_collision
from Components.subject import Player, Client

def is_valide_movement(new_coordinate: tuple[float, float], matrix: Matrix) -> bool:
    
    valid_movement = True
    is_collision_return = is_collision(new_coordinate, matrix)
    
    if len(is_collision_return) == 0:
        valid_movement = True
    if entity_type.wall in is_collision_return:
        valid_movement = False
    if entity_type.player in is_collision_return:
        valid_movement = False
    if entity_type.shelf in is_collision_return:
        valid_movement = False
    if entity_type.shelf in is_collision_return and entity_type.destination in is_collision_return:
        valid_movement = True
    if entity_type.shelf in is_collision_return and entity_type.client in is_collision_return:
        valid_movement = True
        
    return valid_movement

def is_valide_pick(player: Player, client: Client) -> bool:
    
    player_max_capacity = player.get_max_capacity()
    player_clients_loaded = player.get_client_loaded()
    client_volume = client.get_volume()
    
    clients_load_height = 0
    clients_load_width = 0
    
    if len(player_clients_loaded) != 0:
        for player in player_clients_loaded:
            clients_load_height += player.volume["height"]
            clients_load_width += player.volume["width"]

        player_remain_capacity = (player_max_capacity["height"] * player_max_capacity["width"]) - (clients_load_height * clients_load_width)
    
    else:
        player_remain_capacity = player_max_capacity["height"] * player_max_capacity["width"]

    condition_remain_volume= player_remain_capacity >= (client_volume["height"] * client_volume["width"])
    condition_valide_height= player_max_capacity["height"] >= client_volume["height"]
    condition_valide_width= player_max_capacity["width"] >= client_volume["width"]

    if condition_remain_volume and condition_valide_height and condition_valide_width:
        return True
    else:
        return False
