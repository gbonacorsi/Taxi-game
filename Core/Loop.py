
from Presentation.Turtle.display_system import Screen
from Managers.world_manager import World
from Configuration.setup import RENDER_ENGINE, RENDERING

class loop:

    def __init__ (self, world: World, screen : Screen | None = None, is_level_completed: bool = False, close_game: bool = False) -> None:
        self.world = world
        self.screen = screen if RENDER_ENGINE == "Turtle" and RENDERING == True else None
        self.is_level_completed = is_level_completed
        self.close_game = close_game

    def run (self):
        while not self.close_game:

            if self.is_level_completed == False:
                self.screen.update() if self.screen else None

            elif self.is_level_completed:
                self.world.reset() if self.world else None
                self.screen.reset() if self.screen else None

                self.is_level_completed = False

    def set_level_status(self, status: bool) -> None:
        self.is_level_completed = status
