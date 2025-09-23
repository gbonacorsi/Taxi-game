import turtle
import environement as env
import elements as elm
import view as render
import levels
from utils import choose_random_position
from elements import BLINK_COUNTER, BLINK_SPEED
from rules import GameChart
import os

# Configuration
SHOW_GRAPHICS = False  # Set to False for background mode

# Game variables
picked_client = False
drop_destination = False

# Load levels - only if graphics are enabled
if SHOW_GRAPHICS:
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Taxi Game")
    wn.setup(width=800, height=800)
    wn.tracer(0)
else:
    # Hide the turtle graphics window
    os.environ['SDL_VIDEODRIVER'] = 'dummy'  # For some systems
    wn = turtle.Screen()
    wn.setup(width=1, height=1)  # Minimal window
    wn.tracer(0)
    try:
        wn.getcanvas().master.withdraw()  # Hide the window
    except:
        pass

pen=env.Pen()
player=elm.Player()
client=elm.Client() 
destination=elm.Destination()
text_display = render.TextDisplay()
score_display = render.ScoreDisplay()
map=levels.maps[0]
gameChart=GameChart(player, client, destination, score_display)

pen.hideturtle()
player.hideturtle()
client.hideturtle()
destination.hideturtle()
   
# Display game - only if graphics are enabled
if SHOW_GRAPHICS:
    render.setup_maze(text_display, score_display, pen, map, player, client, destination, gameChart.total_reward)

client_position= choose_random_position()
destination_position = choose_random_position()

client.goto(client_position)
destination.goto(destination_position)

# Keyboard listeners - only if graphics are enabled
if SHOW_GRAPHICS:
    turtle.listen()
    turtle.onkey(gameChart.go_up, "w")
    turtle.onkey(gameChart.go_up, "Up")
    turtle.onkey(gameChart.go_down, "s")
    turtle.onkey(gameChart.go_down, "Down")
    turtle.onkey(gameChart.go_left, "a")
    turtle.onkey(gameChart.go_left, "Left")
    turtle.onkey(gameChart.go_right, "d")
    turtle.onkey(gameChart.go_right, "Right")
    turtle.onkey(gameChart.client_picking, "e")
    turtle.onkey(gameChart.client_dropping, "q")

# Main game loop
while True:
    while not gameChart.drop_destination:    
        if SHOW_GRAPHICS:
            wn.update()
            # Handle blinking only if graphics are shown
            BLINK_COUNTER += 1
            if BLINK_COUNTER >= BLINK_SPEED:
                client.blink()       
                BLINK_COUNTER = 0
        # In background mode, the game logic continues without graphics

    client_position= choose_random_position()
    destination_position = choose_random_position()    

    client.goto(client_position)
    destination.goto(destination_position)
    gameChart.drop_destination = False