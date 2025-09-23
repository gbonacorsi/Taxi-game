import turtle
from Components.objects import Player
from Managers.movement_system import Movement


class KeyBoard_input:
    
    def __init__(self, players: list,):
        self.player = None
        self.player_index = 0
        self.players = players
        pass

    def select_player(self, index: int) -> None:
        self.player = self.players[index] if 0 <= index < len(self.players) else self.players[0]
        self.player_index = index if 0 <= index < len(self.players) else 0

    def go_up(self) -> None:
        if self.player:
            coordinate = Movement(self.player.position)
            player = player.instance
            player.
            self.player.set_position(new_coordinate)
            
            

    def controls(self) -> None:
        """Setup keyboard controls for the game."""
        turtle.listen()
        
        # Movement controls - WASD and Arrow keys
        turtle.onkey(self.game_chart.go_up, "w")
        turtle.onkey(self.game_chart.go_up, "Up")
        turtle.onkey(self.game_chart.go_down, "s")
        turtle.onkey(self.game_chart.go_down, "Down")
        turtle.onkey(self.game_chart.go_left, "a")
        turtle.onkey(self.game_chart.go_left, "Left")
        turtle.onkey(self.game_chart.go_right, "d")
        turtle.onkey(self.game_chart.go_right, "Right")
        
        # Action controls
        turtle.onkey(self.select_player(0), "1")
        turtle.onkey(self.select_player(1), "2")
        turtle.onkey(self.select_player(2), "3")
        turtle.onkey(self.select_player(3), "4")
        turtle.onkey(self.select_player(4), "5")