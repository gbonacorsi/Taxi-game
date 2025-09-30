from Configuration.data_structure import actions
from Managers.movement_system import Movement2D
from Managers.world_manager import World
from enum import Enum

class actions(Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    pick = "pick"
    drop = "drop"
    

class EventManager:

    def __init__(self, world: World):
        self.world: World = world
        self.player = None
        
    def select_client(self, index: int) -> None:
        self.player = self.world.return_player_from_id(index)

    def action(self, action: actions) -> None:
             
        movement_listener = Movement2D(self.world, self.player)

        if actions.up == action:
            print("go_up")
            movement_listener.go_up()
            print(self.world.matrix)
        elif actions.down == action:
            print("go_down")
            movement_listener.go_down()
            print(self.world.matrix)
        elif actions.left == action:
            print("go_left")        
            movement_listener.go_left()
            print(self.world.matrix)
        elif actions.right == action:
            print("go_right")
            movement_listener.go_right()
            print(self.world.matrix)