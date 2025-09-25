from Configuration.data_structure import actions
from Configuration.setup import RENDERING, RENDER_ENGINE
from Configuration.data_structure import FieldRecord
from Components.subject import Player
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import Screen
from Managers.world_manager import World
from loop import loop
from Systems.Input_management import KeyBoard

class Engine:
    def __init__(self, matrix: list | None = None, world: World | None = None):
        self.world = world
        self.matrix = matrix
        pass
         
    def initialize(self):
        world = World()
        self.matrix = world.generate_new_world()

    def run(self, RENDERING=RENDERING, RENDER_ENGINE=RENDER_ENGINE):
            
        if RENDERING==True and RENDER_ENGINE == "Turtle":
            game_screen = Screen()
            game_screen.initialize()
            game_screen.render()
            keyboard_listener = KeyBoard(self.world)
            keyboard_listener.run()
            
        loop_instance = loop(world=self.world, screen=game_screen if RENDERING==True and RENDER_ENGINE == "Turtle" else None, is_level_completed=False, close_game=False)
        loop_instance.run()
        
    def action(self, player: FieldRecord, action: actions):
        
        movement_listener = Movement2D(self.world, player)
        
        if actions.up == action:
            movement_listener.go_up()
        elif actions.down == action:
            movement_listener.go_down()
        elif actions.left == action:
            movement_listener.go_left()
        elif actions.right == action:
            movement_listener.go_right()

