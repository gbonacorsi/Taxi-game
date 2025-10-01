from enum import Enum
from Configuration.data_structure import actions
from Components.subject import Player
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import Screen


class EventManager:

    def __init__(self, world: World, display: Screen | None = None) -> None:
        self.world: World = world
        self.player : Player | None = None
        self.display: Screen | None = display
        
    def select_client(self, index: int) -> None:
        self.player = self.world.players[index - 1].instance

    def action(self, action: actions) -> None:
             
        movement_listener = Movement2D(self.world, self.player)

        if actions.up == action:
            print("go_up")
            movement_listener.go_up()
        elif actions.down == action:
            print("go_down")
            movement_listener.go_down()
        elif actions.left == action:
            print("go_left")        
            movement_listener.go_left()
        elif actions.right == action:
            print("go_right")
            movement_listener.go_right()