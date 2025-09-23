import render_system as rs
import turtle
from ui_system import TextDisplay, ScoreDisplay, DistanceDisplay
from render_system import Display_game

class Screen:
    
    def __init__(self, label):
        self.label = label
        self.title= TextDisplay("white")
        self.controls= TextDisplay("white")
        self.elements= TextDisplay("white")
        self.mission= TextDisplay("white")
        self.score_display= ScoreDisplay(label["score"])
        self.distance_display= DistanceDisplay(label["distance"])
        self.display_game= Display_game()

    def initialize(self) -> None:
        turtle.clearscreen()
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Taxi Game")
        wn.setup(width=800, height=800)
        
    def render(self, map: list[list[str]] = [[]]) -> None:
        self.title.display_text(-380, 370, self.label["title"], 24)
        self.controls.display_text(-380, 350, self.label["controls"], 14)
        self.elements.display_text(-380, 330, self.label["elements"], 12)
        self.mission.display_text(-380, -380, self.label["mission"], 14)
        self.score_display.display_score(40, 350,0)
        self.distance_display.display_distance(40, 290,0,0)
        self.display_game.render((-240, 180),map)
        self.mission.display_text(-380, -380, self.label["mission"], 14)
    
    def update_score(self, score: int) -> None:
        self.score_display.update_score(score)

    def update_distance(self, distance_client: int, distance_destination: int) -> None:
        self.distance_display.update_distance(distance_client, distance_destination)
