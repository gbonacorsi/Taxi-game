import turtle
from Configuration.data_structure import actions
from Managers.world_manager import World
from Core.event_manager import EventManager

class KeyBoard:
    
    def __init__(self, world: World) -> None:
        self.player_index = 0
        self.payer = None
        self.event_manager = EventManager(world) 

    def listen(self) -> None:
        turtle.listen()
    
    def select_player_1(self) -> None:
        self.player_index = 1
        self.player = self.event_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_2(self) -> None:
        self.player_index = 2
        self.player = self.event_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_3(self) -> None:
        self.player_index = 3
        self.player = self.event_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_4(self) -> None:
        self.player_index = 4
        self.player = self.event_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_5(self) -> None:
        self.player_index = 4
        self.player = self.event_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

      
    
    def go_up(self) -> None:
        self.event_manager.action(actions.up)
    
    def go_down(self) -> None:
        self.event_manager.action(actions.down)
    
    def go_left(self) -> None:
        self.event_manager.action(actions.left)
    
    def go_right(self) -> None:
        self.event_manager.action(actions.right)
        

    def run(self) -> None:
        
        turtle.onkey(self.go_up, "w")
        turtle.onkey(self.go_down, "s")
        turtle.onkey(self.go_left, "a")
        turtle.onkey(self.go_right, "d")

        turtle.onkey(self.select_player_1, "1")
        turtle.onkey(self.select_player_2, "2")
        turtle.onkey(self.select_player_3, "3")
        turtle.onkey(self.select_player_4, "4")
        turtle.onkey(self.select_player_5, "5")


 