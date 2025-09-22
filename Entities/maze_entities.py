import turtle

class Destination(turtle.Turtle):
    def __init__(self, destination_parameters: dict = {"shape": None, "color": None, "speed": 0}) -> None:
        super().__init__()
        self.shape(destination_parameters["shape"])
        self.color(destination_parameters["color"])
        self.penup()
        self.speed(destination_parameters["speed"])

class Client(turtle.Turtle):
    def __init__(self, client_parameters: dict = {"shape": None, "color": None, "speed": 0, "blink_state": None, "blink_colors": None}) -> None:
        super().__init__()
        self.shape(client_parameters["shape"])
        self.color(client_parameters["color"])
        self.penup()
        self.speed(client_parameters["speed"])
        self.blink_state = client_parameters["blink_state"]
        self.blink_colors = client_parameters["blink_colors"]

class Player(turtle.Turtle):
    def __init__(self, player_parameters: dict = {"shape": "square", "color": "Gold", "speed": 0}) -> None:
        super().__init__()
        self.shape(player_parameters["shape"])
        self.color(player_parameters["color"])
        self.penup()
        self.speed(player_parameters["speed"])
        
class Wall(turtle.Turtle):
    def __init__(self, wall_parameters: dict = {"shape": "square", "color": "White", "speed": 0}) -> None:
        super().__init__()
        self.shape(wall_parameters["shape"])
        self.color(wall_parameters["color"])
        self.penup()
        self.speed(wall_parameters["speed"])

class Shelf(turtle.Turtle):
    def __init__(self, shelf_parameters: dict = {"shape": "square", "color": "DarkGray", "speed": 0}) -> None:
        super().__init__()
        self.shape(shelf_parameters["shape"])
        self.color(shelf_parameters["color"])
        self.penup()
        self.speed(shelf_parameters["speed"])