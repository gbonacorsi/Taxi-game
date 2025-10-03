from operator import index
import turtle
from Managers.world_manager import World
from Configuration.data_structure import ComponentRecord, entity_type
from Configuration.setup import SPACE_BETWEEN_CELLS, MAZE
from Presentation.Turtle.components_display import WallDisplay, ShelfDisplay, PlayerDisplay, ClientDisplay, DestinationDisplay

class Display_game:

    def __init__(self, world: World) -> None:
        self.world = world
        self.players_display=[]
        self.clients_display=[]
        self.destinations_display=[]
        self.walls_display=[]
        self.shelves_display=[]
        self.players_display_id = 1
        self.clients_display_id = 1
        self.destinations_display_id = 1
        self.walls_display_id = 1
        self.shelves_display_id = 1

    def generate_components_display(self, id :int, component_list: list[None | ComponentRecord], 
                                    display_list: list[None | ClientDisplay | DestinationDisplay | WallDisplay | ShelfDisplay | PlayerDisplay]) -> None:

        for component in component_list:
            component : ComponentRecord = component
            component_position = component.instance.get_position()

            if component.type == entity_type.wall:
                component_display: WallDisplay = WallDisplay(component.get_values()["id"])
            elif component.type == entity_type.player:
                component_display: PlayerDisplay = PlayerDisplay(component.get_values()["id"])
            elif component.type == entity_type.client:
                component_display: ClientDisplay = ClientDisplay(component.get_values()["id"])
            elif component.type == entity_type.destination:
                component_display: DestinationDisplay = DestinationDisplay(component.get_values()["id"])
            elif component.type == entity_type.shelf:
                component_display: ShelfDisplay = ShelfDisplay(component.get_values()["id"])

            x = MAZE["X"] + (component_position[0] * SPACE_BETWEEN_CELLS) + component_position[0]
            y = MAZE["Y"]  - (component_position[1] * SPACE_BETWEEN_CELLS) - component_position[1]
            component_display.goto(x, y)
            record_display = [component_position, component_display]

            display_list.append(record_display)
        
        id += 1

    def maze_render(self, initial_coor: tuple = (MAZE["X"], MAZE["Y"]), map: list[list[str]] = [[]], square_interval: int = SPACE_BETWEEN_CELLS) -> None:

        self.generate_components_display(self.walls_display_id, self.world.walls, self.walls_display)
        self.generate_components_display(self.shelves_display_id, self.world.shelves, self.shelves_display)
        self.generate_components_display(self.players_display_id, self.world.players, self.players_display)
        self.generate_components_display(self.clients_display_id, self.world.clients, self.clients_display)
        self.generate_components_display(self.destinations_display_id, self.world.destinations, self.destinations_display)

    def change_blink(self) -> None:
        print("Blink Change Triggered")
        for client_display_record in self.clients_display:
            client_display : ClientDisplay= client_display_record[1]
            client_display.blink()
            client_display.stamp()

    def move_display_record(self, old_position: tuple[int, int], new_position: tuple[int, int],
                    component: ComponentRecord) -> None:
        
        component_type = component.get_values()["type"]
        
        if component_type == entity_type.client:
            index, display_component = self.return_from_position(old_position, self.clients_display)
            display_component : ClientDisplay = self.clients_display.pop(index)[1]
            self.clients_display.append([new_position, display_component])
        elif component_type == entity_type.destination:
            index, display_component = self.return_from_position(old_position, self.destinations_display)
            display_component : DestinationDisplay = self.destinations_display.pop(index)[1]
            self.destinations_display.append([new_position, display_component])
        elif component_type == entity_type.wall:
            index, display_component = self.return_from_position(old_position, self.walls_display)
            display_component : WallDisplay = self.walls_display.pop(index)[1]
            self.walls_display.append([new_position, display_component])
        elif component_type == entity_type.shelf:
            index, display_component = self.return_from_position(old_position, self.shelves_display)
            display_component : ShelfDisplay = self.shelves_display.pop(index)[1]
            self.shelves_display.append([new_position, display_component])
        elif component_type == entity_type.player:
            index, display_component = self.return_from_position(old_position, self.players_display)
            display_component : PlayerDisplay = self.players_display.pop(index)[1]
            self.players_display.append([new_position, display_component])

        x = MAZE["X"] + (new_position[0] * SPACE_BETWEEN_CELLS) + new_position[0]
        y = MAZE["Y"]  - (new_position[1] * SPACE_BETWEEN_CELLS) - new_position[1]
        display_component.clear()
        display_component.goto(x, y)
        display_component.stamp()
    
    def return_from_position(self, position: tuple[int, int], 
                         display_list: list[None | ClientDisplay | DestinationDisplay | WallDisplay | ShelfDisplay | PlayerDisplay]) -> None:

        index = 0
        for record in display_list:
            if record[0] == position:
                return index, record[1]
            index += 1
        
        return None
    
    def remove_display_record(self, position: tuple[int, int]) -> None:

        index, display_component = self.return_from_position(position, self.clients_display)
        if display_component != None:
            self.clients_display.pop(index)
            display_component.clear()
            display_component.hideturtle()
        
        index, display_component = self.return_from_position(position, self.destinations_display)
        if display_component != None:
            self.destinations_display.pop(index)
            display_component.clear()
            display_component.hideturtle()