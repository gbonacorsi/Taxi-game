from Configuration.data_structure import ComponentRecord, actions, entity_type
from Configuration.setup import RENDERING, RENDER_ENGINE, BLINK_SPEED
from Components.subject import Player
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Managers.scoring_system import ScoringSystem
from Presentation.Turtle.display_system import TurtleScreen
from Managers.Inventory_system import pick_item, drop_item
from Core.state_manager import State_manager

class EventManager:

    def __init__(self, world: World, display: TurtleScreen | None = None) -> None:
        self.world: World = world
        self.player : Player | None = None
        self.display: TurtleScreen | None = display
        self.scoring_system : ScoringSystem = ScoringSystem()
        self.blink_counter : int = 0
        self.state_manager : State_manager = State_manager()
        self.list_client_loaded : list[ComponentRecord] = []
        self.explored_cells : list[tuple[int, int]] = []

    def turtle_blinking(self, screen: TurtleScreen) -> None:

        if self.blink_counter >= BLINK_SPEED:
            self.blink_counter = 0
            screen.change_blink()
        else:
            self.blink_counter += 1
    
    def move_player(self, world: World, action: actions, player: Player = None) -> None:

        movement_system_player = Movement2D(world, player)

        if actions.up == action:
            current_position, new_position, moved = movement_system_player.go_up()
        elif actions.down == action:
            current_position, new_position, moved = movement_system_player.go_down()
        elif actions.left == action:   
            current_position, new_position, moved = movement_system_player.go_left()
        elif actions.right == action:
            current_position, new_position, moved = movement_system_player.go_right()

        self.scoring_system.add_penalty_for_travel()
        if moved == False:
            self.scoring_system.add_penalty_for_collision()
            self.display.update_score(self.scoring_system.get_score())

        if new_position not in self.explored_cells:
            self.scoring_system.add_bonus_for_new_cell()
            
        self.explored_cells.append(new_position)
        
        return current_position, new_position, moved

    def move_client(self, world: World, action: actions, client: ComponentRecord) -> None:
        
        movement_system_client = Movement2D(world, client)
        
        if actions.up == action:
            current_position, new_position, moved = movement_system_client.go_up()
        elif actions.down == action:
            current_position, new_position, moved = movement_system_client.go_down()
        elif actions.left == action:   
            current_position, new_position, moved = movement_system_client.go_left()
        elif actions.right == action:
            current_position, new_position, moved = movement_system_client.go_right()
        
        return current_position, new_position, moved

    def update_rendering(self, current_position: tuple[float, float], new_position: tuple[float, float], component: ComponentRecord) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.move_display_record(current_position, new_position, component)
            self.display.update_score(self.scoring_system.get_score())
    
    def remove_rendering_client_and_destination(self, current_position: tuple[float, float]) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.remove_display_record(current_position)
            
    def update_scoring(self) -> int:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.update_score(self.scoring_system.get_score())

    def pick_client(self, player: Player, world: World) -> list:
        self.list_client_loaded = pick_item(player, world.matrix)
        self.state_manager.status_client_loaded(player, self.list_client_loaded)


    def drop_client(self, player: Player, world: World) -> None:
        self.state_manager.status_client_drop(player, self.list_client_loaded)
        condition_valid_drop , destination= drop_item(player.get_values()["instance"], player.get_values()["instance"].get_position(), world)

        if condition_valid_drop == True:
            self.scoring_system.add_reward_for_correct_drop()
            self.state_manager.status_destination_arrived(destination)
        else:
            self.scoring_system.add_penalty_for_wrong_drop()

        return condition_valid_drop

    def reset_score(self) -> None:
        self.scoring_system.reset_score()

    def reset_rendering(self) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.reset()

    def all_destinations_reached(self) -> bool:

        destinations = self.world.destinations
        reached = False
        
        value_vdv = []
        for destination in destinations:
            value_vdv.append(destination.get_values()["instance"].arrived)
        
        if all(value_vdv):
            reached = True
            
        return reached
    
    def reset_world(self):
        self.world.reset()
        self.world.generate_random_components(entity_type.destination)
        self.world.generate_random_components(entity_type.client)
        self.world.link_clients_destination()
        self.reset_score()