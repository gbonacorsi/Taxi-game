from random import randint

from Configuration.setup import *
from Configuration.data_structure import *
from Components.maze_components import *
from Components.objects import *
from Components.subject import *
from Asset.levels import maps

class World:
    def __init__(self) -> None:
        
        self.map = maps[MAP_INDEX]
        self.matrix = []
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

    def choose_random_position(self) -> tuple[float, float]:

        map_id=MAP_INDEX
        y = randint(0, len(maps[map_id]) - 1)
        x = randint(0, len(maps[map_id][y]) - 1)
        
        return (x, y)

    def is_empty(self, coordinate: tuple[float, float]) -> bool:
        coordinates_value = self.matrix[coordinate[1]][coordinate[0]]
        return True if coordinates_value == [] else False

    def contain_type(self, coordinate: tuple[float, float], entity_type: entity_type) -> bool:

        is_found = False

        coordinates_value = self.matrix[coordinate[1]][coordinate[0]]
        
        for value in coordinates_value:
            if value.type in entity_type.value:
                is_found = True

        return is_found

    def generate_random_components(self, id:int, number: int, component_type: entity_type) -> None:

        for i in range(number-1):
            
            position = self.choose_random_position()
            while self.is_empty(position) == False:
                position = self.choose_random_position()
            
            if component_type == entity_type.player:
                new_player = Player(self.players_id, position[0], position[1])
                record=FieldRecord(self.players_id, entity_type.player, new_player, (position[0], position[1]))
                self.players.append(new_player)
                self.matrix[position[1]][position[0]] = [record]
                self.maps[position[1]][position[0]] = "P",
                self.players_id += 1

            elif component_type == entity_type.client:
                new_client = Client(self.clients_id, position[0], position[1])
                record=FieldRecord(self.clients_id, entity_type.client, new_client, (position[0], position[1]))
                self.clients.append(new_client)
                self.matrix[position[1]][position[0]] = [record]
                self.maps[position[1]][position[0]] = "C"
                self.clients_id += 1
            
            while self.contain_type(position, entity_type.shelf) == False:   
                position = self.choose_random_position()
            if component_type == entity_type.destination:
                new_destination = Destination(self.destinations_id, position[0], position[1])
                record=FieldRecord(self.destinations_id, entity_type.destination, new_destination, (position[0], position[1]))
                self.destinations.append(new_destination)
                self.matrix[position[1]][position[0]] = [record]
                self.maps[position[1]][position[0]] = "X"
                self.destinations_id += 1

    def generate_new_world(self) -> None:

        y_range= len(self.map)
        x_range= len(self.map[0])

        for y in range (y_range):
            row=[]
            
            for x in range (x_range):
                    
                    character = self.map[y][x]
                    
                    if character == "#":
                        shelf = Shelf(self.shelves_id, x, y)
                        record=FieldRecord(self.shelves_id, entity_type.shelf, shelf, (x,y))
                        row.append([record])
                        self.shelves.append(shelf)
                        self.shelves_id += 1
                        
                    elif character == "!":
                        wall = Wall(self.walls_id, x, y)
                        record=FieldRecord(self.walls_id, entity_type.wall, wall, (x,y))
                        row.append([record])
                        self.walls.append(wall)
                        self.walls_id += 1
                                        
                    else:
                        row.append([])
            
            self.matrix.append(row)
            
        self.generate_random_components(self.clients_id, CLIENTS_NUMBER, entity_type.client)
        self.generate_random_components(self.players_id, PLAYERS_NUMBER, entity_type.player)
        self.generate_random_components(self.destinations_id, PLAYERS_NUMBER, entity_type.destination)

    def add_component(self, new_coordinate: tuple[float, float], field: FieldRecord) -> None:

        if self.matrix is not None:
            self.matrix[new_coordinate[1]][new_coordinate[0]].append(field)

    def remove_component(self, old_coordinate: tuple[float, float], field: FieldRecord) -> None:

        if self.matrix is not None:
            self.matrix[old_coordinate[1]][old_coordinate[0]].remove(field)

    def return_field_from_coordinate(self, coordinate: tuple[float, float], component_type: entity_type, in_matrix: bool = True) -> FieldRecord | None:

        if in_matrix:
            if self.matrix is not None:
                coordinates_value = self.matrix[coordinate[1]][coordinate[0]]
                
                for field in coordinates_value:
                    if field.type in component_type.value and field.position == coordinate:
                        return field
        else:
            if component_type == entity_type.player:
            
                for field in self.players:
                    if field.position == coordinate:
                        return field

            if component_type == entity_type.client:
            
                for field in self.clients:
                    if field.position == coordinate:
                        return field

            if component_type == entity_type.destination:
            
                for field in self.destinations:
                    if field.position == coordinate:
                        return field

            if component_type == entity_type.wall:
            
                for field in self.walls:
                    if field.position == coordinate:
                        return field

            if component_type == entity_type.shelf:
            
                for field in self.shelves:
                    if field.position == coordinate:
                        return field
        return None

    def reset(self) -> None:

        self.map = maps[MAP_INDEX]
        self.matrix = []
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
        self.generate_new_world()