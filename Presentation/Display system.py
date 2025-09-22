import turtle
from environement import Pen, shelfs_coordinates, walls_coordinates
from elements import Player, Client, Destination

TITLE = "TAXI GAME"
CONTROLS = "Controls: press w to go Up, s to go Down, a to go Left, d to go Right, e to Pick, q to Drop"
ELEMENTS = "Gold square = Player, Yellow Circle = Client, Orange Circle = Destination"
MISSION = "Collect the client and deliver to destination!"

class TextDisplay(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.score = 0
    
    def display_text(self, x, y, text, font_size=16):
        self.goto(x, y)
        self.write(text, align="left", font=("Arial", font_size, "normal"))
    
class ScoreDisplay(TextDisplay):
    def __init__(self):
        self.x, self.y = 0, 0
        super().__init__()

    def display_score(self,x,y,total_reward: int) -> None:
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(f"Score: {total_reward}", align="left", font=("Arial", 18, "bold"))
    
    def update_score(self, total_reward: int) -> None:
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"Score: {total_reward}", align="left", font=("Arial", 18, "bold"))

class DistanceDisplay(TextDisplay):
    def __init__(self):
        self.x, self.y = 0, 0
        super().__init__()

    def display_distance(self,x,y, distance_client: float, distance_destination: float) -> None:
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(f"Distance Taxi to Client: {int(distance_client)}\nDistance Client to Destination: {int(distance_destination)}", align="left", font=("Arial", 16, "bold"))

    def update_distance(self, distance_client: float, distance_destination: float) -> None:
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"Distance Taxi to Client: {int(distance_client)}\nDistance Client to Destination: {int(distance_destination)}", align="left", font=("Arial", 16, "bold"))

def setup_maze(text_display: TextDisplay, 
               score_display: ScoreDisplay, 
               distance_display: DistanceDisplay,
               pen: Pen, 
               level, 
               player: Player, 
               client: Client, 
               destination: Destination,
               total_reward: int) -> None:

    text_display.display_text(-380, 350, TITLE, 20)
    text_display.display_text(-380, 240, CONTROLS, 14)
    text_display.display_text(-380, 220, ELEMENTS, 12)
    score_display.display_score(40, 350,total_reward)
    distance_display.display_distance(40, 290,player.distance(client), player.distance(destination))
    


    text_display.display_text(-380, -380, MISSION, 14)
         
    pen.showturtle()
    player.showturtle()
    client.showturtle()
    destination.showturtle()
    