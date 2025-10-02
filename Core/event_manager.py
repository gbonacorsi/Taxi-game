from Configuration.data_structure import actions, ComponentRecord
from Configuration.setup import RENDERING, RENDER_ENGINE
from Components.subject import Player
from Managers.world_manager import World
from Managers.movement_system import Movement2D
from Presentation.Turtle.display_system import TurtleScreen


class EventManager:

    def __init__(self, world: World, display: TurtleScreen | None = None) -> None:
        self.world: World = world
        self.player : Player | None = None
        self.display: TurtleScreen | None = display

    def update_rendering(self, current_position: tuple[float, float], new_position: tuple[float, float], component: ComponentRecord) -> None:
        if RENDERING == True and RENDER_ENGINE == "Turtle":
            self.display.move_display_record(current_position, new_position, component)
