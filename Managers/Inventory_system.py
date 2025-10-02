from Components.subject import Player,Client
from Utils.matrix_system import Matrix
from Managers.validation_system import is_valide_pick

def pick_item(player: Player, matrix: Matrix) -> None:
    
    position_pick = player.get_position()
    list_components = matrix.return_position_records(position_pick)
    clients = matrix.filter(key="type", criteria="client", index=None, list_of_component=list_components)

    clients=[]
    for client in clients:
        clients.append(client)
    
    for client in clients:
        if is_valide_pick(player, client):
            player.pick(client)

def drop_item(player: Player, client: Client) -> None:
    
    player.drop(client)
    
    