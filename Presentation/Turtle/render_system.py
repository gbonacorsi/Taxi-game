import turtle

class DestinationDisplay(turtle.Turtle):
    def __init__(self, x:float, y:float, destination_parameters: dict = {"shape": None, "color": None, "speed": 0}) -> None:
        super().__init__()
        self.x=x,
        self.y=y,
        self.shape(destination_parameters["shape"])
        self.color(destination_parameters["color"])
        self.penup()
        self.speed(destination_parameters["speed"])
        
        def got_up(self):
            self.sety(self.ycor() + 24)
        def go_down(self):
            self.sety(self.ycor() - 24)
        def go_left(self):
            self.setx(self.xcor() - 24)
        def go_right(self):
            self.setx(self.xcor() + 24)

class ClientDisplay(turtle.Turtle):
    def __init__(self, x:float, y:float, client_parameters: dict = {"shape": None, "color": None, "speed": 0, "blink_state": None, "blink_colors": None}) -> None:
        super().__init__()
        self.x=x,
        self.y=y,
        self.shape(client_parameters["shape"])
        self.color(client_parameters["color"])
        self.penup()
        self.speed(client_parameters["speed"])
        self.blink_state = client_parameters["blink_state"]
        self.blink_colors = client_parameters["blink_colors"]
    
        def got_up(self):
            self.sety(self.ycor() + 24)
        def go_down(self):
            self.sety(self.ycor() - 24)
        def go_left(self):
            self.setx(self.xcor() - 24)
        def go_right(self):
            self.setx(self.xcor() + 24)

class PlayerDisplay(turtle.Turtle):
    def __init__(self, x:float, y:float, player_parameters: dict = {"shape": "square", "color": "Gold", "speed": 0}) -> None:
        super().__init__()
        self.x=x,
        self.y=y,
        self.shape(player_parameters["shape"])
        self.color(player_parameters["color"])
        self.penup()
        self.speed(player_parameters["speed"])

        def got_up(self):
            self.sety(self.ycor() + 24)
        def go_down(self):
            self.sety(self.ycor() - 24)
        def go_left(self):
            self.setx(self.xcor() - 24)
        def go_right(self):
            self.setx(self.xcor() + 24)
        
class WallDisplay(turtle.Turtle):
    def __init__(self, wall_parameters: dict = {"shape": "square", "color": "White", "speed": 0}) -> None:
        super().__init__()
        self.x=0,
        self.y=0,
        self.shape(wall_parameters["shape"])
        self.color(wall_parameters["color"])
        self.penup()
        self.speed(wall_parameters["speed"])

        def got_up(self):
            self.sety(self.ycor() + 24)
        def go_down(self):
            self.sety(self.ycor() - 24)
        def go_left(self):
            self.setx(self.xcor() - 24)
        def go_right(self):
            self.setx(self.xcor() + 24)

class ShelfDisplay(turtle.Turtle):
    def __init__(self, x:float, y:float, shelf_parameters: dict = {"shape": "square", "color": "DarkGray", "speed": 0}) -> None:
        super().__init__()
        self.x=x,
        self.y=y,
        self.shape(shelf_parameters["shape"])
        self.color(shelf_parameters["color"])
        self.penup()
        self.speed(shelf_parameters["speed"])

        def got_up(self):
            self.sety(self.ycor() + 24)
        def go_down(self):
            self.sety(self.ycor() - 24)
        def go_left(self):
            self.setx(self.xcor() - 24)
        def go_right(self):
            self.setx(self.xcor() + 24)

class Display_game:
    
    def maze_render(self, initial_coor: tuple = (-240, 180), map: list[list[str]] = [[]], square_interval: int = 24) -> None:
        y_range= len(map)
        x_range= len(map[0])
        
        for y in range (y_range):
            for x in range (x_range):
                character = map[y][x]
                screen_x = initial_coor[0] + (x * square_interval)
                screen_y = initial_coor[1] - (y * square_interval)

                if character == "#":
                    shelf = ShelfDisplay(x, y)
                    shelf.goto(screen_x, screen_y)
                    shelf.stamp()

                if character == "!":
                    wall = WallDisplay(x, y)
                    wall.goto(screen_x, screen_y)
                    wall.stamp()
                    
                if character == "P":
                    player = PlayerDisplay(x,y)
                    player.goto(screen_x, screen_y)
                    player.stamp()
                    
                if character == "c":
                    client = ClientDisplay(x,y)
                    client.goto(screen_x, screen_y)
                    client.stamp()
                    
                if character == "X":
                    destination = DestinationDisplay(x,y)
                    destination.goto(screen_x, screen_y)
                    destination.stamp()
                    
