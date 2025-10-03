import turtle
from enum import Enum
from Configuration.setup import DESTINATION, CLIENT, PLAYER, WALL, SHELF, BLINK_COLORS

class DestinationDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, destination_parameters: dict = {"shape": DESTINATION["SHAPE"], "color": DESTINATION["COLOR"], "speed": DESTINATION["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(destination_parameters["shape"])
        self.color(destination_parameters["color"])
        self.penup()
        self.speed(destination_parameters["speed"])

class ClientDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, client_parameters: dict = {"shape": CLIENT["SHAPE"], "color": CLIENT["COLOR"], "speed": CLIENT["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(client_parameters["shape"])
        self.color(client_parameters["color"])
        self.penup()
        self.speed(client_parameters["speed"])
        self.blink_state = False
    
    def blink(self) -> None:
        self.blink_state = not self.blink_state
        if self.blink_state:
            self.color(BLINK_COLORS[0])
        else:
            self.color(BLINK_COLORS[1])

class PlayerDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, player_parameters: dict = {"shape": PLAYER["SHAPE"], "color": PLAYER["COLOR"], "speed": PLAYER["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(player_parameters["shape"])
        self.color(player_parameters["color"])
        self.penup()
        self.speed(player_parameters["speed"])

class WallDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, wall_parameters: dict = {"shape": WALL["SHAPE"], "color": WALL["COLOR"], "speed": WALL["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(wall_parameters["shape"])
        self.color(wall_parameters["color"])
        self.penup()
        self.speed(wall_parameters["speed"])

class ShelfDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, shelf_parameters: dict = {"shape": SHELF["SHAPE"], "color": SHELF["COLOR"], "speed": SHELF["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(shelf_parameters["shape"])
        self.color(shelf_parameters["color"])
        self.penup()
        self.speed(shelf_parameters["speed"])

class components_display(Enum):
    wall = WallDisplay
    shelf = ShelfDisplay
    player = PlayerDisplay
    client = ClientDisplay
    destination = DestinationDisplay