import turtle
from Configuration.data_structure import actions
from Managers.world_manager import World

class KeyBoard:
    
    def __init__(self, players: list, simulation: World) -> None:
        self.player = None
        self.player_index = 0
        self.players = players
        self.simulation = simulation
        pass

    def select_player(self, index: int) -> None:
        self.player = self.players[index] if 0 <= index < len(self.players) else self.players[0]
        self.player_index = index if 0 <= index < len(self.players) else 0
            
    def run(self) -> None:
        """Setup keyboard controls for the game."""
        turtle.listen()
        
        # Movement controls - WASD and Arrow keys
        turtle.onkey(self.simulation.action(self.player, actions.up), "w")
        turtle.onkey(self.simulation.action(self.player, actions.down), "s")
        turtle.onkey(self.simulation.action(self.player, actions.left), "a")
        turtle.onkey(self.simulation.action(self.player, actions.right), "d")

        # Action controls
        turtle.onkey(self.select_player(0), "1")
        turtle.onkey(self.select_player(1), "2")
        turtle.onkey(self.select_player(2), "3")
        turtle.onkey(self.select_player(3), "4")
        turtle.onkey(self.select_player(4), "5")