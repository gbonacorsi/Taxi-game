#import Core.dependencies

from Configuration.setup import *
from Configuration.data_structure import *
from Asset.levels import *
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Core.loop import loop
from Presentation.Turtle.display_system import Screen
from Systems.Input_management import KeyBoard

class Engine:
    def __init__(self, matrix: list | None = None, world: World | None = None):
        self.world = world
        self.matrix = matrix
        pass
         
    def initialize(self):
        self.world = World()
        self.matrix = self.world.generate_new_world()

    def run(self, RENDERING=RENDERING, RENDER_ENGINE=RENDER_ENGINE):
            
        if RENDERING==False: 

            print("""The simulation is running in non-graphical mode. Type: 'exit' to quit.""")
            input_command = input("Press command: ")
            
            if input_command == "exit":
                exit()  
        
        elif RENDERING==True and RENDER_ENGINE == "Turtle":
            print("coucou")
            game_screen = Screen(self.world)
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

