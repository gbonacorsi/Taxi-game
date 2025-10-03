from Configuration.data_structure import ComponentRecord, entity_type
from Utils.matrix_system import Matrix
from Managers.world_manager import World
from Managers.collision_system import is_collision
from Components.subject import Player, Client

def is_valide_movement(new_coordinate: tuple[float, float], matrix: Matrix, component_type: entity_type) -> bool:
    
    valid_movement = True
    
    if component_type == entity_type.player:
        is_collision_return = is_collision(new_coordinate, matrix)
        
        if len(is_collision_return) != 0:
            if entity_type.wall in is_collision_return:
                valid_movement = False
            elif entity_type.player in is_collision_return:
                valid_movement = False
            elif entity_type.shelf in is_collision_return and entity_type.destination in is_collision_return:
                valid_movement = True
            elif entity_type.shelf in is_collision_return and entity_type.client in is_collision_return:
                valid_movement = True
            elif entity_type.shelf in is_collision_return:
                valid_movement = False
        
    return valid_movement

def is_valide_pick(player: Player, client: Client) -> bool:
    
    player_max_capacity = player.get_max_capacity()
    player_clients_loaded = player.get_client_loaded()
    client_volume = client.get_volume()
    
    clients_load_height = 0
    clients_load_width = 0
    
    if len(player_clients_loaded) != 0:
        for client_component in player_clients_loaded:
            client_data = client_component.get_values()["instance"].get_volume()
            clients_load_height += client_data["height"]
            clients_load_width += client_data["width"]

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

def is_valide_drop(player_position: tuple[int, int], world: World) -> bool:

    list_destination = world.destinations
    list_components_at_position = world.matrix.return_position_records(player_position)

    if list_components_at_position != None:

        for position, destination_data in list_components_at_position:
            if destination_data in list_destination:
                return destination_data, True

    return None, False
