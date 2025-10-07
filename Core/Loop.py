from Managers.world_manager import World
from Presentation.Turtle.display_system import TurtleScreen
from Configuration.setup import RENDER_ENGINE, RENDERING, INPUT_TYPE
from Systems.Input_management import KeyBoard
from Core.event_manager import EventManager
from Core.game_manager import GameManager
from Network.server import GameServer

class loop:

    def __init__ (self, world: World, screen : TurtleScreen | None = None) -> None:
        self.world = world
        self.screen = screen
        self.event_manager = EventManager(self.world, self.screen)
        self.game_manager = GameManager(self.world, self.screen, self.event_manager)
        self.server = GameServer(self.game_manager)

    def run (self):
        
        self.game_manager.init()
        
        condition_rendering = RENDERING and RENDER_ENGINE == "Turtle"
        condition_input_keyboard = INPUT_TYPE.value == "keyboard"
        condition_input_server = INPUT_TYPE.value == "server"
        

        # Initialize keyboard
        if condition_input_keyboard:
            keyboard = KeyBoard(self.world, self.game_manager)
            keyboard.listen()
        
        try:
                
            while True:
                
                # Rendering
                if condition_rendering:
                    self.event_manager.turtle_blinking(self.screen)
                    self.screen.update()
                
                # Listen to keyboard
                if condition_input_keyboard:
                    keyboard.run()
                
                if condition_input_server:
                    self.server.run()

                # Check end of level
                if self.event_manager.all_destinations_reached():
                    self.game_manager.level_completed()

        finally:
            print("Game closed.")
            exit()