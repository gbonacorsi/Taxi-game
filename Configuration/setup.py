# Import reale perché usiamo lang a runtime
from Asset.labels import lang
from enum import Enum

class input_type(Enum):
    KEYBOARD = "keyboard"
    SERVER = "server"
    
# GAME SETTINGS
MAP_INDEX = 0
PLAYERS_NUMBER = 2                          # when Input_Type = KEYBOARD -> max 5 players
CLIENTS_NUMBER = 2
INPUT_TYPE = input_type.KEYBOARD            # input_type.KEYBOARD or input_type.SERVER      
RENDERING = True
RENDER_ENGINE = "Turtle" 

# PLAYER SETTINGS

PLAYER_CAPACITY = {
    "regular": {"height": 1, "width": 1},
}
PLAYER_DEFAULT_CAPACITY = "regular"

# CLIENT SETTINGS

CLIENT_VOLUME = {
    "regular": {"height": 1, "width": 1},
}
CLIENT_DEFAULT_VOLUME = "regular"

# LABEL LANGUAGE
LANGUAGE = lang.ENG.value

# Scoring
REWARD_CORRECT_DROP = 120
MALUS_TRAVEL = -1
MALUS_WRONG_DROP = -20

# DISPLAY
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_BGCOLOR = "black"

# GRID SETTINGS
SPACE_BETWEEN_CELLS = 24

# BLINK SETTINGS
BLINK_SPEED = 10
BLINK_COLORS = ["yellow", "red"]
BLINK_DELAY = 0.1

# DISPLAY COMPONENTS

TITLE = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 24,
    "FONT_TYPE": "bold",
    "FONT_COLOR": "white",
    "X": -360,
    "Y": 340
}

CONTROL = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 14,
    "FONT_TYPE": "normal",
    "FONT_COLOR": "white",
    "X": -360,
    "Y": 260
}

ELEMENT = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 14,
    "FONT_TYPE": "normal",
    "FONT_COLOR": "white",
    "X": -360,
    "Y": 240
}

MISSION = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 14,
    "FONT_TYPE": "normal",
    "FONT_COLOR": "white",
    "X": -360,
    "Y": -390
}

DISPLAY_SCORE = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 18,
    "FONT_TYPE": "bold",
    "FONT_COLOR": "white",
    "X": 140,
    "Y": 340
}

MAZE = {
    "X": -280,
    "Y": 200
}

PLAYER = {
    "SHAPE": "square",
    "COLOR": "gold",
    "SPEED": 0}

CLIENT = {
    "SHAPE": "circle",
    "COLOR": "yellow",
    "SPEED": 0}

DESTINATION = {
    "SHAPE": "triangle",
    "COLOR": "orange",
    "SPEED": 0
}

WALL = {
    "SHAPE": "square",  
    "COLOR": "white",
    "SPEED": 0
}

SHELF = {
    "SHAPE": "square",  
    "COLOR": "LightGray",
    "SPEED": 0
}

