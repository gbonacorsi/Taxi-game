import turtle
from Configuration.data_structure import actions
from Managers.world_manager import World
from Core.game_manager import GameManager

class KeyBoard:

    def __init__(self, world: World, game_manager: GameManager) -> None:
        self.player_index = 0
        self.payer = None
        self.game_manager = game_manager

    def listen(self) -> None:
        turtle.listen()
    
    def select_player_1(self) -> None:
        self.player_index = 0
        self.player = self.game_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_2(self) -> None:
        self.player_index = 1
        self.player = self.game_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_3(self) -> None:
        self.player_index = 2
        self.player = self.game_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_4(self) -> None:
        self.player_index = 3
        self.player = self.game_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

    def select_player_5(self) -> None:
        self.player_index = 4
        self.player = self.game_manager.select_client(self.player_index)
        print(f"Player {self.player_index + 1} selected")

      
    
    def go_up(self) -> None:
        self.game_manager.action(actions.up)
    
    def go_down(self) -> None:
        self.game_manager.action(actions.down)
    
    def go_left(self) -> None:
        self.game_manager.action(actions.left)
    
    def go_right(self) -> None:
        self.game_manager.action(actions.right)
    
    def pick(self) -> None:
        self.game_manager.action(actions.pick)
    
    def drop(self) -> None:
        self.game_manager.action(actions.drop)

    def run(self) -> None:
        
        turtle.onkey(self.go_up, "w")
        turtle.onkey(self.go_down, "s")
        turtle.onkey(self.go_left, "a")
        turtle.onkey(self.go_right, "d")
        turtle.onkey(self.pick, "p")
        turtle.onkey(self.drop, "o")

        turtle.onkey(self.select_player_1, "1")
        turtle.onkey(self.select_player_2, "2")
        turtle.onkey(self.select_player_3, "3")
        turtle.onkey(self.select_player_4, "4")
        turtle.onkey(self.select_player_5, "5")


 