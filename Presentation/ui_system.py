import turtle

class TextDisplay(turtle.Turtle):
    def __init__(self, color: str, format: dict = {"align": "left", "font":"Arial", "font_size": 16, "font_type": "normal"}):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(color)
        self.speed(0)
        self.format = format
        self.x, self.y = 0, 0
        
        """Display text on the screen at specified coordinates.
        
        Args:
            color: Text color
            Format: Text format dictionary with keys:
                - align: Text alignment ("left", "center", "right") (default: "left")
                - font: Font type (default: "Arial")    
                - font_size: Font size (default: 16)
                - font_type: Font style ("normal", "bold", "italic") (default: "normal")
        """

    def display_text(self, x: float, y: float, text: str):

        """Display text on the screen at specified coordinates.

        Args:
            x: X-coordinate
            y: Y-coordinate
            text: Text to display
        """
        
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(text, align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))

class ScoreDisplay(TextDisplay):
    def __init__(self, label : dict = {"score": "score"}, format: dict = {"align": "left", "font":"Arial", "font_size": 18, "font_type": "bold"}):
        self.label = label
        self.format = format
        super().__init__()
    
    """Display and update the player's score on the screen.
    
    Args:
        label: Label for the score display in the language of your choice (default: "Score") 
        format: Text format dictionary with keys:
            - align: Text alignment ("left", "center", "right") (default: "left")      
            - font: Font type (default: "Arial")
            - font_size: Font size (default: 18)
            - font_type: Font style ("normal", "bold", "italic") (default: "bold")
    """
        
    def display_score(self, x: float, y: float,total_reward: int) -> None:
        
        """Display game score
        
        Args:
            x: x coordinate
            y: y coordinate
            total_reward: Current total reward (score)"""
        
        self.clear()
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
        super().__init__()
        
    """Display and update distances to client and destination.
    
    Args:
        label: Label for the distance on the language of your choice (default: {"distance_client": "Distance to Client", "distance_destination": "Distance to Destination"})
        format: Text format dictionary with keys:
            - align: Text alignment ("left", "center", "right") (default: "left")      
            - font: Font type (default: "Arial")
            - font_size: Font size (default: 16)
            - font_type: Font style ("normal", "bold", "italic") (default: "bold")
    """

    def display_distance(self, x: float, y: float, distance_client: float, distance_destination: float) -> None:
        
        """Display distances to client and destination.
        Args:
            x: x coordinate
            y: y coordinate
            distance_client: Distance to client
            distance_destination: Distance to destination
        """
        
        self.clear()
        self.x, self.y = x, y
        self.goto(self.x, self.y)
        self.write(f"{self.label['distance_client']}: {int(distance_client)}\n{self.label['distance_destination']}: {int(distance_destination)}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))

    def update_distance(self, distance_client: float, distance_destination: float) -> None:
        
        """Update distances to client and destination.
        Args:
            distance_client: Distance to client
            distance_destination: Distance to destination
        """
        
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"{self.label['distance_client']}: {int(distance_client)}\n{self.label['distance_destination']}: {int(distance_destination)}", align=self.format["align"], font=(self.format["font"], self.format["font_size"], self.format["font_type"]))
