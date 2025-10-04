from Configuration.data_structure import ComponentRecord

class State_manager:

    def __init__(self) -> None:
        pass

    def status_client_loaded(self, player: ComponentRecord, clients: list[ComponentRecord]) -> None:

        for client in clients:
            client.get_values()["instance"].loaded == True
        player.get_values()["instance"].clients_loaded_state = True

    def status_client_drop(self, player: ComponentRecord, clients: list[ComponentRecord]) -> None:

        for client in clients:
            client.get_values()["instance"].loaded == False

        if player.get_values()["instance"].clients_loaded != None:
            player.get_values()["instance"].clients_loaded_state = False

    def status_destination_arrived(self, destination: ComponentRecord) -> None:
        destination.get_values()["instance"].arrived = True