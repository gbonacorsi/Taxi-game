from Configuration.data_structure import actions, ComponentRecord
from Configuration.setup import RENDERING
from Components.subject import Player
from Managers.world_manager import World
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

    def action(self, action: actions, player: Player = None) -> None:

        if player is None:
            player : ComponentRecord= self.player

        client_loaded = player.get_values()["instance"].clients_loaded

        if actions.up == action:
            # Move subjects
            current_position_player, new_position_player, moved_player = self.event_manager.move_player(self.world, actions.up, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                for client in client_loaded:
                    self.event_manager.move_client(self.world, actions.up, client)

            # Update rendering
            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_player, new_position_player, client)

                      
        elif actions.down == action:
            # Move subjects
            current_position_player, new_position_player, moved_player = self.event_manager.move_player(self.world, actions.down, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                for client in client_loaded:
                    self.event_manager.move_client(self.world, actions.down, client)

            # Update rendering
            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_player, new_position_player, client)

        elif actions.left == action:   
            # Move subjects
            current_position_player, new_position_player, moved_player = self.event_manager.move_player(self.world, actions.left, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                for client in client_loaded:
                    self.event_manager.move_client(self.world, actions.left, client)

            # Update rendering
            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_player, new_position_player, client)

        elif actions.right == action:
            # Move subjects
            current_position_player, new_position_player, moved_player = self.event_manager.move_player(self.world, actions.right, player)
            if moved_player == True and self.has_player_loaded_client(player)[0]:
                for client in client_loaded:
                    self.event_manager.move_client(self.world, actions.right, client)

            # Update rendering
            if moved_player == True and RENDERING == True:
                self.event_manager.update_rendering(current_position_player, new_position_player, player)
                
                if moved_player == True and self.has_player_loaded_client(player)[0]:                    
                    for client in client_loaded:
                        self.event_manager.update_rendering(current_position_player, new_position_player, client)

        
        elif actions.pick == action:

            self.event_manager.pick_client(player, self.world)
        
        elif actions.drop == action:
            
            condition_dropping = self.event_manager.drop_client(player, self.world)

            if RENDERING == True:
                self.event_manager.update_scoring()
                
            if RENDERING == True and condition_dropping:
                self.event_manager.remove_rendering_client_and_destination(player.get_values()["instance"].get_position())
                self.event_manager.update_scoring()
    
    def level_completed(self):
        print("Level completed!")
        self.event_manager.reset_world()
        
        if RENDERING == True:
            self.event_manager.reset_rendering()
