"""
Game Constants and Configuration

Central location for all game constants and configuration values.
"""

# Screen Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_BGCOLOR = "black"
SCREEN_TITLE = "Taxi Game"

# Game Colors
PLAYER_COLOR = "gold"
CLIENT_COLOR = "yellow" 
DESTINATION_COLOR = "orange"
WALL_COLOR = "white"
PATH_COLOR = "black"

# Game Mechanics
MOVEMENT_PENALTY = -1
DELIVERY_REWARD = 120
WRONG_DELIVERY_PENALTY = -20

# Animation Settings
BLINK_SPEED = 10
ANIMATION_DELAY = 0.1

# Level Configuration
DEFAULT_LEVEL = 0

# Grid Settings
GRID_SIZE = 24
CELL_SIZE = 24

# Controls Help Text
CONTROLS_TEXT = """
🎮 CONTROLS:
• WASD or Arrow Keys: Move taxi
• E: Pick up client (when nearby)
• Q: Drop off client (at destination)

🎯 OBJECTIVE:
Pick up clients (yellow circle) and deliver them 
to their destinations (orange circle) while 
maximizing your score!

📊 SCORING:
• Movement: -1 point
• Successful delivery: +120 points  
• Wrong delivery: -20 points
"""