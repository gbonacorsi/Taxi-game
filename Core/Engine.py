from Configuration.setup import RENDER, RENDER_ENGINE
from Asset.labels import LABELS
from Managers.world_manager import World

class Engine:
    def __init__(self, matrix: list | None = None, world: World | None = None):
        self.world = world
        self.matrix = matrix
        pass
        
    def initialize(self):
        world = World()
        self.matrix = world.generate_new_world()

    def run(self, RENDER):
        while RENDER_ENGINE == "Turtle":
            if self.game_screen:
                self.game_screen.render()
            

