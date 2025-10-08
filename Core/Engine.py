from Configuration.setup import RENDERING, RENDER_ENGINE
from Managers.world_manager import World
from Core.loop import loop
from Presentation.Turtle.display_system import TurtleScreen

class Engine:
    def __init__(self, matrix: list | None = None, world: World | None = None):
        self.world = world
        self.matrix = matrix
         
    def initialize(self):
        self.world = World()
        self.matrix = self.world.generate_new_world()

    def run(self):
            
        if RENDERING==True and RENDER_ENGINE == "Turtle":
            
            game_screen = TurtleScreen(self.world)
            game_screen.initialize()
            game_screen.render()      
            
            loop_instance = loop(world=self.world, screen=game_screen)
            loop_instance.run()
        
        if RENDERING==False:
            
            loop_instance = loop(world=self.world)
            loop_instance.run()


