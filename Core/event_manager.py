from Configuration.data_structure import ComponentRecord
from Configuration.setup import RENDERING, RENDER_ENGINE, BLINK_SPEED
from Components.subject import Player
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import TurtleScreen


class EventManager:

    def __init__(self, world: World, display: TurtleScreen | None = None) -> None:
        self.world: World = world
        self.player : Player | None = None
        self.display: TurtleScreen | None = display
        self.blink_counter : int = 0

    def turtle_client_blinking(self, screen: TurtleScreen) -> None:

        if self.blink_counter >= BLINK_SPEED:
            self.blink_counter = 0
            screen.change_blink()
        else:
            self.blink_counter += 1
        
    def update_rendering(self, current_position: tuple[float, float], new_position: tuple[float, float], component: ComponentRecord) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.move_display_record(current_position, new_position, component)
    
    def remove_rendering_client_and_destination(self, current_position: tuple[float, float]) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.remove_display_record(current_position)
