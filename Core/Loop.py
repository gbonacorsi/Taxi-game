from Managers.world_manager import World
from Presentation.Turtle.display_system import TurtleScreen
from Configuration.setup import RENDER_ENGINE, RENDERING, BLINK_SPEED
from Systems.Input_management import KeyBoard
from Core.event_manager import EventManager

def turtle_client_blinking(screen: TurtleScreen):
    blink_counter = 0
    
    if blink_counter >= BLINK_SPEED:
        blink_counter = 0
        screen.change_blink()
    else:
        blink_counter += 1


class loop:

    def __init__ (self, world: World, screen : TurtleScreen | None = None) -> None:
        self.world = world
        self.screen = screen
        self.is_level_completed : bool = False

    def run (self):
        
        if RENDERING==True and RENDER_ENGINE == "Turtle":
            
            event_manager = EventManager(self.world, self.screen)
            event_manager.select_client(0)  # Select the first player by default
            
            keyboard = KeyBoard(self.world, event_manager)
            keyboard.listen()
            
            try:
                
                while True:
                    turtle_client_blinking(self.screen)
                    self.screen.update()
                    keyboard.run()

            finally:
                print("Game closed.")
                exit()