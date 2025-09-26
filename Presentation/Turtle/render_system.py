import turtle
from enum import Enum
from Managers.world_manager import World
from Configuration.data_structure import actions, entity_type, FieldDisplay, FieldRecord
from Configuration.setup import SPACE_BETWEEN_CELLS, DESTINATION, CLIENT, PLAYER, WALL, SHELF, BLINK_COLORS

def action(action: actions, display_entity: object | None = None) -> actions | None:
    if action == actions.up:
        display_entity.sety(display_entity.ycor() + SPACE_BETWEEN_CELLS)
        display_entity.y += 1
        display_entity.goto(display_entity.x, display_entity.y)
    elif action == actions.down:
        display_entity.sety(display_entity.ycor() - SPACE_BETWEEN_CELLS)
        display_entity.y -= 1
        display_entity.goto(display_entity.x, display_entity.y)
    elif action == actions.left:
        display_entity.setx(display_entity.xcor() - SPACE_BETWEEN_CELLS)
        display_entity.x -= 1
        display_entity.goto(display_entity.x, display_entity.y)
    elif action == actions.right:
        display_entity.setx(display_entity.xcor() + SPACE_BETWEEN_CELLS)
        display_entity.x += 1
        display_entity.goto(display_entity.x, display_entity.y)
        
        return action

def update_field_matrix(matrix, position: tuple[int, int], new_values: dict, entity_type: entity_type) -> None:
    pass
    #field_matrix: FieldRecord = matrix.return_field_from_coordinate(position, entity_type)
    #field_matrix.update_values(new_values)

class DestinationDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, destination_parameters: dict = {"shape": DESTINATION["SHAPE"], "color": DESTINATION["COLOR"], "speed": DESTINATION["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(destination_parameters["shape"])
        self.color(destination_parameters["color"])
        self.penup()
        self.speed(destination_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class ClientDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, client_parameters: dict = {"shape": CLIENT["SHAPE"], "color": CLIENT["COLOR"], "speed": CLIENT["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(client_parameters["shape"])
        self.color(client_parameters["color"])
        self.penup()
        self.speed(client_parameters["speed"])
        self.blink_state = False
    
    def blink(self) -> None:
        self.blink_state = not self.blink_state
        if self.blink_state:
            self.color(BLINK_COLORS[0])
        else:
            self.color(BLINK_COLORS[1])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class PlayerDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, player_parameters: dict = {"shape": PLAYER["SHAPE"], "color": PLAYER["COLOR"], "speed": PLAYER["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(player_parameters["shape"])
        self.color(player_parameters["color"])
        self.penup()
        self.speed(player_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)
        
class WallDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, wall_parameters: dict = {"shape": WALL["SHAPE"], "color": WALL["COLOR"], "speed": WALL["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(wall_parameters["shape"])
        self.color(wall_parameters["color"])
        self.penup()
        self.speed(wall_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class ShelfDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, shelf_parameters: dict = {"shape": SHELF["SHAPE"], "color": SHELF["COLOR"], "speed": SHELF["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.shape(shelf_parameters["shape"])
        self.color(shelf_parameters["color"])
        self.penup()
        self.speed(shelf_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class Display_game:

    def __init__(self, world: World) -> None:
        self.world = world
        self.matrix = world.matrix
        self.players=[]
        self.clients=[]
        self.destinations=[]
        self.walls=[]
        self.shelves=[]
        self.players_id = 1
        self.clients_id = 1
        self.destinations_id = 1
        self.walls_id = 1
        self.shelves_id = 1
    
    def maze_render(self, initial_coor: tuple = (-240, 180), map: list[list[str]] = [[]], square_interval: int = SPACE_BETWEEN_CELLS) -> None:


        y_range= len(map)
        x_range= len(map[0])
        
        for y in range (y_range):
            for x in range (x_range):
                character = map[y][x]
                screen_x = initial_coor[0] + (x * square_interval)
                screen_y = initial_coor[1] - (y * square_interval)

                if character == "#":
                    shelf = ShelfDisplay(self.shelves_id)
                    
                    field_display = FieldDisplay(self.shelves_id, entity_type.shelf, ShelfDisplay, (x,y))
                    self.shelves.append(field_display)
                    self.shelves_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.shelves_id
                    }, entity_type.shelf)
                    
                    shelf.goto(screen_x, screen_y)
                    shelf.stamp()

                if character == "!":
                    wall = WallDisplay(self.walls_id)
                    self.walls.append(wall)
                    self.walls_id += 1
                    update_field_matrix(self.world, (x,y), {
                        "grid_id": self.walls_id
                    }, entity_type.wall)
                    
                    wall.goto(screen_x, screen_y)
                    wall.stamp()
                    
                if character == "P":
                    player = PlayerDisplay(self.players_id)
                    self.players.append(player)
                    self.players_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.players_id
                    }, entity_type.player)
                    
                    player.goto(screen_x, screen_y)
                    player.stamp()
                    
                if character == "C":
                    client = ClientDisplay(self.clients_id)
                    self.clients.append(client)
                    self.clients_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.clients_id
                    }, entity_type.client)
                    
                    client.goto(screen_x, screen_y)
                    client.stamp()
                    
                if character == "X":
                    destination = DestinationDisplay(self.destinations_id)
                    self.destinations.append(destination)
                    self.destinations_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.destinations_id
                    }, entity_type.destination)
                    
                    destination.goto(screen_x, screen_y)
                    destination.stamp()
                    
    def change_blink(self) -> None:
        for client in self.clients:
            client.blink()
            client.stamp()
            
class displays(Enum):
    Player = PlayerDisplay
    Client = ClientDisplay
    Destination = DestinationDisplay
    Wall = WallDisplay
    Shelf = ShelfDisplay