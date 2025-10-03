from Components.subject import Player
from Configuration.data_structure import ComponentRecord, entity_type, component_record_keys
from Managers.world_manager import World
from Utils.matrix_system import Matrix
from Managers.validation_system import is_valide_pick, is_valide_drop

def pick_item(player: ComponentRecord, matrix: Matrix) -> None:
    
    position_pick = player.get_values()["instance"].get_position()
    list_components = matrix.return_position_records(position_pick)
    client_data_list = matrix.filter(component_record_keys.type, entity_type.client, index=None, list_of_component=list_components)
    
    if client_data_list != None:
        for position, client_record in client_data_list:
            client_instance = client_record["instance"]
            client_component : ComponentRecord = ComponentRecord(
                id=client_record["id"],
                type=client_record["type"],
                instance=client_record["instance"]
            )

            player : Player = player.get_values()["instance"]
            if is_valide_pick(player, client_instance):
                player.clients_loaded.append(client_component)

def drop_item(player: Player, player_position: tuple[int, int], world: World) -> None:

    destination, condition_valid_drop = is_valide_drop(player_position, world)
    
    list_clients_loaded = player.get_client_loaded()
    if condition_valid_drop and len(list_clients_loaded) > 0:
        for client in list_clients_loaded:
            world.destinations.remove(destination)
            player.clients_loaded.remove(client)
            
            world.matrix.remove_record(player_position, client)
            world.matrix.remove_record(player_position, destination)
    
    elif not condition_valid_drop and len(list_clients_loaded) > 0:
        for client in list_clients_loaded:
            player.clients_loaded.remove(client)
    
    return condition_valid_drop
        
            
        
            