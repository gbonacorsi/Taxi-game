from Configuration.data_structure import actions, ComponentRecord
from Configuration.setup import RENDERING
from Components.subject import Player
from Managers import movement_system
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import TurtleScreen
from Core.event_manager import EventManager

class GameManager:

    def __init__(self, world: World, display: TurtleScreen | None = None, event_manager: EventManager | None = None) -> None:
        self.world: World = world
        self.event_manager: EventManager = event_manager
        self.player : Player | None = None

    def select_client(self, index: int = 0) -> None:
        self.player = self.world.players[index]
    
    def init(self) -> None:
        self.select_client()

    def has_player_loaded_client(self, player: ComponentRecord = None) -> tuple[bool, list]:

        if player is None:
            player = self.player
            
            
        client_loaded = player.get_values()["instance"].clients_loaded
        criteri_client_loaded = True if len(client_loaded) > 0 else False

        if criteri_client_loaded:
            return True, client_loaded
        else:
            return False, client_loaded

    def move_player(self, action: actions, player: Player = None) -> None:
        if player is None:
            player = self.player

        movement_system = Movement2D(self.world, player)
        
        if actions.up == action:
            current_position, new_position, moved = movement_system.go_up()
        elif actions.down == action:
            current_position, new_position, moved = movement_system.go_down()
        elif actions.left == action:   
            current_position, new_position, moved = movement_system.go_left()
        elif actions.right == action:
            current_position, new_position, moved = movement_system.go_right()
        
        return current_position, new_position, moved

    def move_client(self, action: actions, player: Player) -> None:
        
        if player is None:
            player = self.player

        client_loaded = player.clients_loaded
        
        
        for client in client_loaded:
            movement_system = Movement2D(self.world, client) 
            if actions.up == action:
                current_position, new_position, moved = movement_system.go_up()
            elif actions.down == action:
                current_position, new_position, moved = movement_system.go_down()
            elif actions.left == action:   
                current_position, new_position, moved = movement_system.go_left()
            elif actions.right == action:
                current_position, new_position, moved = movement_system.go_right()

        return current_position, new_position

    def action(self, action: actions, player: Player = None) -> None:

        if player is None:
            player = self.player

        if actions.up == action:
            current_position_player, new_position_player, moved_player = self.move_player(actions.up, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                current_position_client, new_position_client = self.move_client(actions.up, player)

            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:
                    client_loaded = player.clients_loaded
                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_client, new_position_client, client)

                      
        elif actions.down == action:
            current_position_player, new_position_player, moved_player = self.move_player(actions.down, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                current_position_client, new_position_client = self.move_client(actions.down, player)

            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:
                    client_loaded = player.clients_loaded
                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_client, new_position_client, client)
                
        elif actions.left == action:   
            current_position_player, new_position_player, moved_player = self.move_player(actions.left, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                current_position_client, new_position_client = self.move_client(actions.left, player)

            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:
                    client_loaded = player.clients_loaded
                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_client, new_position_client, client)

        elif actions.right == action:
            current_position_player, new_position_player, moved_player = self.move_player(actions.right, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                current_position_client, new_position_client = self.move_client(actions.right, player)

            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:
                    client_loaded = player.clients_loaded
                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_client, new_position_client, client)
        
