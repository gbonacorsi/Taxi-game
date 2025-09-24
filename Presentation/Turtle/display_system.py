import turtle
from Asset.levels import maps
from Asset.labels import LABELS
from Configuration.setup import *
from ui_system import TextDisplay, ScoreDisplay, DistanceDisplay
from render_system import Display_game

class Screen:
    
    def __init__(self):
        self.label = LABELS[LANGUAGE.value]
        self.title= TextDisplay(color=TITLE["FONT_COLOR"], format={"align": TITLE["FONT_ALIGN"], "font": TITLE["FONT_NAME"], "font_size": TITLE["FONT_SIZE"], "font_type": TITLE["FONT_TYPE"]}),
        self.controls= TextDisplay(color=CONTROL["FONT_COLOR"], format={"align": CONTROL["FONT_ALIGN"], "font": CONTROL["FONT_NAME"], "font_size": CONTROL["FONT_SIZE"], "font_type": CONTROL["FONT_TYPE"]}),
        self.elements= TextDisplay(color=ELEMENT["FONT_COLOR"], format={"align": ELEMENT["FONT_ALIGN"], "font": ELEMENT["FONT_NAME"], "font_size": ELEMENT["FONT_SIZE"], "font_type": ELEMENT["FONT_TYPE"]}),
        self.mission= TextDisplay(color=MISSION["FONT_COLOR"], format={"align": MISSION["FONT_ALIGN"], "font": MISSION["FONT_NAME"], "font_size": MISSION["FONT_SIZE"], "font_type": MISSION["FONT_TYPE"]}),
        self.score_display= ScoreDisplay(self.label["score"], format={"align": DISPLAY_SCORE["FONT_ALIGN"], "font": DISPLAY_SCORE["FONT_NAME"], "font_size": DISPLAY_SCORE["FONT_SIZE"], "font_type": DISPLAY_SCORE["FONT_TYPE"]}),
        self.distance_display= DistanceDisplay(self.label["distance"], format={"align": DISPLAY_DISTANCE["FONT_ALIGN"], "font": DISPLAY_DISTANCE["FONT_NAME"], "font_size": DISPLAY_DISTANCE["FONT_SIZE"], "font_type": DISPLAY_DISTANCE["FONT_TYPE"]}),
        self.display_game= Display_game()
    
    def initialize(self) -> None:
        turtle.clearscreen()
        wn = turtle.Screen()
        wn.bgcolor(SCREEN_BGCOLOR)
        wn.title(self.label["title"])
        wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        
    def render(self, map = maps[MAP_INDEX]) -> None:
        self.title.display_text(TITLE["X"], TITLE["Y"], self.label["title"])
        self.controls.display_text(CONTROL["X"], CONTROL["Y"], self.label["controls"])
        self.elements.display_text(ELEMENT["X"], ELEMENT["Y"], self.label["elements"])
        self.mission.display_text(MISSION["X"], MISSION["Y"], self.label["mission"])
        self.score_display.display_score(DISPLAY_SCORE["X"], DISPLAY_SCORE["Y"], 0)
        self.distance_display.display_distance(DISPLAY_DISTANCE["X"], DISPLAY_DISTANCE["Y"], 0, 0)
        self.display_game.maze_render((MAZE["X"], MAZE["Y"]), map)
        self.mission.display_text(MISSION["X"], MISSION["Y"], self.label["mission"])
    
    def update_score(self, score: int) -> None:
        self.score_display.update_score(score)

    def update_distance(self, distance_client: int, distance_destination: int) -> None:
        self.distance_display.update_distance(distance_client, distance_destination)
