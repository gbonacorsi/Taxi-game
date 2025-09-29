
from Presentation.Turtle.display_system import Screen
from Managers.world_manager import World
from Configuration.setup import RENDER_ENGINE, RENDERING, BLINK_DELAY, BLINK_SPEED
from Systems.Input_management import KeyBoard

class loop:

    def __init__ (self, world: World, screen : Screen | None = None, is_level_completed: bool = False, close_game: bool = False) -> None:
        self.world = world
        self.screen = screen if RENDER_ENGINE == "Turtle" and RENDERING == True else None
        self.is_level_completed = is_level_completed
        self.close_game = close_game

    def run (self):
        
        blink_counter = 0
        keyboard = KeyBoard(self.world)
        keyboard.listen()
        keyboard.run()
        
        while not self.close_game:
            
            self.screen.update() if self.screen else None
            
            if blink_counter >= BLINK_SPEED:
                blink_counter = 0
                self.screen.change_blink()
            else:
                blink_counter += 1

    def set_level_status(self, status: bool) -> None:
        self.is_level_completed = status
