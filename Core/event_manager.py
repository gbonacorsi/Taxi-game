from enum import Enum
from Configuration.data_structure import actions, ComponentRecord
from Configuration.setup import RENDERING, RENDER_ENGINE
from Components.subject import Player
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import TurtleScreen
from Presentation.Turtle.render_system import Display_game


class EventManager:

    def __init__(self, world: World, display: TurtleScreen | None = None) -> None:
        self.world: World = world
        self.player : Player | None = None
        self.display: TurtleScreen | None = display
        #self.game_display : Display_game | None = self.display.display_game
        
    def select_client(self, index: int) -> None:
        self.player = self.world.players[index]

    def update_rendering(self, current_position: tuple[float, float], new_position: tuple[float, float], component: ComponentRecord) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.move_display_record(current_position, new_position, component)

    def action(self, action: actions) -> None:
             
        movement_listener = Movement2D(self.world, self.player)

        if actions.up == action:
            current_position, new_position = movement_listener.go_up()
            self.update_rendering(current_position, new_position, self.player)
            
        elif actions.down == action:
            current_position, new_position = movement_listener.go_down()
            self.update_rendering(current_position, new_position, self.player)

        elif actions.left == action:   
            current_position, new_position = movement_listener.go_left()
            self.update_rendering(current_position, new_position, self.player)
            
        elif actions.right == action:
            current_position, new_position = movement_listener.go_right()
            self.update_rendering(current_position, new_position, self.player)