from Configuration.setup import RENDER_TURTLE, LANGUAGE
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

    def run(self):
        """Main game loop"""
        while RENDER_TURTLE:
            if self.game_screen:
                self.game_screen.render()
            
            # Aggiorna logica di gioco
            if self.game_controller:
                self.game_controller.update_game()

