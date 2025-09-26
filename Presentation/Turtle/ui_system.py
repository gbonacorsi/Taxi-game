import turtle

class TextDisplay(turtle.Turtle):
    def __init__(self, color: str = "White", format: dict = {"align": "left", "font":"Arial", "font_size": 16, "font_type": "normal"}):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(color)
        self.speed(0)
        self.format = format
        self.x, self.y = 0, 0

    def display_text(self, x: float, y: float, text: str):

        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(text, align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))

class ScoreDisplay(TextDisplay):
    def __init__(self, label : dict = {"score": "score"}, format: dict = {"align": "left", "font":"Arial", "font_size": 18, "font_type": "bold"}):
        self.label = label
        super().__init__(format=format)
        
    def display_score(self, x: float, y: float,total_reward: int) -> None:
        
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(f"{self.label}: {total_reward}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))
    
    def update_score(self, total_reward: int) -> None:
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"Score: {total_reward}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))

class DistanceDisplay(TextDisplay):
    def __init__(self, label: dict = {"distance_client": "Distance to Client", "distance_destination": "Distance to Destination"}, format: dict = {"align": "left", "font":"Arial", "font_size": 16, "font_type": "bold"}):
        self.label = label
        self.format = format
        super().__init__(format=format)

    def display_distance(self, x: float, y: float, distance_client: float, distance_destination: float) -> None:
        
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(f"{self.label['distance_client']}: {int(distance_client)}\n{self.label['distance_destination']}: {int(distance_destination)}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))

    def update_distance(self, distance_client: float, distance_destination: float) -> None:
        
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"{self.label['distance_client']}: {int(distance_client)}\n{self.label['distance_destination']}: {int(distance_destination)}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))
