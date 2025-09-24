import turtle
from Configuration.setup import *
from Configuration.data_structure import *
from Managers.world_manager import World

def action(action: actions, display_entity: object | None = None) -> actions | None:
    if action == actions.up:
        display_entity.sety(display_entity.ycor() + SPACE_BETWEEN_CELLS)
        display_entity.y += 1
    elif action == actions.down:
        display_entity.sety(display_entity.ycor() - SPACE_BETWEEN_CELLS)
        display_entity.y -= 1
    elif action == actions.left:
        display_entity.setx(display_entity.xcor() - SPACE_BETWEEN_CELLS)
        display_entity.x -= 1
    elif action == actions.right:
        display_entity.setx(display_entity.xcor() + SPACE_BETWEEN_CELLS)
        display_entity.x += 1
        
        return action

def update_field_matrix(matrix: World, position: tuple[int, int], new_values: dict, entity_type: entity_type) -> None:
    field_matrix = matrix.return_field_from_coordinate(position, entity_type)
    field_matrix.update_values(new_values)

class DestinationDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, x:float, y:float, destination_parameters: dict = {"shape": DESTINATION["SHAPE"], "color": DESTINATION["COLOR"], "speed": DESTINATION["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.x=x,
        self.y=y,
        self.shape(destination_parameters["shape"])
        self.color(destination_parameters["color"])
        self.penup()
        self.speed(destination_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class ClientDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, x:float, y:float, client_parameters: dict = {"shape": CLIENT["SHAPE"], "color": CLIENT["COLOR"], "speed": CLIENT["SPEED"], "blink_state": None, "blink_colors": None}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.x=x,
        self.y=y,
        self.shape(client_parameters["shape"])
        self.color(client_parameters["color"])
        self.penup()
        self.speed(client_parameters["speed"])
        #self.blink_state = client_parameters["blink_state"]
        #self.blink_colors = client_parameters["blink_colors"]
    
        def action(self, action: actions) -> actions | None:
            action(action, self)

class PlayerDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, x:float, y:float, player_parameters: dict = {"shape": PLAYER["SHAPE"], "color": PLAYER["COLOR"], "speed": PLAYER["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.x=x,
        self.y=y,
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
        self.x=0,
        self.y=0,
        self.shape(wall_parameters["shape"])
        self.color(wall_parameters["color"])
        self.penup()
        self.speed(wall_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class ShelfDisplay(turtle.Turtle):
    def __init__(self, grid_id: int, x:float = 0, y:float = 0, shelf_parameters: dict = {"shape": SHELF["SHAPE"], "color": SHELF["COLOR"], "speed": SHELF["SPEED"]}) -> None:
        super().__init__()
        self.grid_id = grid_id
        self.x=x,
        self.y=y,
        self.shape(shelf_parameters["shape"])
        self.color(shelf_parameters["color"])
        self.penup()
        self.speed(shelf_parameters["speed"])

        def action(self, action: actions) -> actions | None:
            action(action, self)

class Display_game:

    def __init__(self, matrix: World | None = None) -> None:
        self.matrix = matrix
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
                    shelf = ShelfDisplay(self.shelves_id, x, y)
                    
                    field_display = FieldDisplay(self.shelves_id, entity_type.shelf, ShelfDisplay, (x,y))
                    self.shelves.append(field_display)
                    self.shelves_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.shelves_id
                    }, entity_type.shelf)
                    
                    shelf.goto(screen_x, screen_y)
                    shelf.stamp()

                if character == "!":
                    wall = WallDisplay(self.walls_id, x, y)
                    self.walls.append(wall)
                    self.walls_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.walls_id
                    }, entity_type.wall)
                    
                    wall.goto(screen_x, screen_y)
                    wall.stamp()
                    
                if character == "P":
                    player = PlayerDisplay(self.players_id, x, y)
                    self.players.append(player)
                    self.players_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.players_id
                    }, entity_type.player)
                    
                    player.goto(screen_x, screen_y)
                    player.stamp()
                    
                if character == "c":
                    client = ClientDisplay(self.clients_id, x, y)
                    self.clients.append(client)
                    self.clients_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.clients_id
                    }, entity_type.client)
                    
                    client.goto(screen_x, screen_y)
                    client.stamp()
                    
                if character == "X":
                    destination = DestinationDisplay(self.destinations_id, x, y)
                    self.destinations.append(destination)
                    self.destinations_id += 1
                    update_field_matrix(self.matrix, (x,y), {
                        "grid_id": self.destinations_id
                    }, entity_type.destination)
                    
                    destination.goto(screen_x, screen_y)
                    destination.stamp()
                    

        def return_field_from_coordinate(self, coordinate: tuple[float, float],component_type: entity_type) -> FieldDisplay | None:

            if entity_type.player == component_type:
            
                for field in self.players:
                    if field.position == coordinate:
                        return field
            
            if entity_type.client == component_type:
            
                for field in self.clients:
                    if field.position == coordinate:
                        return field
            if entity_type.destination == component_type:
            
                for field in self.destinations:
                    if field.position == coordinate:
                        return field
            if entity_type.wall == component_type:
            
                for field in self.walls:
                    if field.position == coordinate:
                        return field
            if entity_type.shelf == component_type:
            
                for field in self.shelves:
                    if field.position == coordinate:
                        return field
                    
            return None