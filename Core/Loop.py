from Managers.world_manager import World
from Presentation.Turtle.display_system import TurtleScreen
from Configuration.setup import RENDER_ENGINE, RENDERING
from Systems.Input_management import KeyBoard
from Core.event_manager import EventManager
from Core.game_manager import GameManager

class loop:

    def __init__ (self, world: World, screen : TurtleScreen | None = None) -> None:
        self.world = world
        self.screen = screen

    def run (self):
        
        if RENDERING==True and RENDER_ENGINE == "Turtle":
            
            event_manager = EventManager(self.world, self.screen)
            game_manager = GameManager(self.world, self.screen, event_manager)
            game_manager.init()

            keyboard = KeyBoard(self.world, game_manager)
            keyboard.listen()
            
            try:
                    
                while True:

                    event_manager.turtle_blinking(self.screen)
                    self.screen.update()
                    keyboard.run()
                    
                    if event_manager.all_destinations_reached():
                        game_manager.level_completed()

            finally:
                print("Game closed.")
                exit()