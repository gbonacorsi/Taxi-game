# Import reale perché usiamo lang a runtime
from Asset.labels import lang

# GAME SETTINGS
MAP_INDEX = 0
PLAYERS_NUMBER = 1     # when RENDER_TURTLE = True -> max 5 players
CLIENTS_NUMBER = 3     
RENDERING = True
RENDER_ENGINE = "Turtle"  # Options: "Turtle"

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
    "Y": 240
}

ELEMENT = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 14,
    "FONT_TYPE": "normal",
    "FONT_COLOR": "white",
    "X": -360,
    "Y": 210
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
    "X": 120,
    "Y": 340
}

DISPLAY_DISTANCE = {
    "FONT_NAME": "Arial",
    "FONT_ALIGN": "left",
    "FONT_SIZE": 14,
    "FONT_TYPE": "normal",
    "FONT_COLOR": "white",
    "X": 120,
    "Y": 290
}

MAZE = {
    "X": -280,
    "Y": 180
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

