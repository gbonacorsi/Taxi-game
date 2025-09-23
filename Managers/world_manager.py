from Asset.levels import maps
from Configuration.setup import MAP_INDEX, CLIENTS_NUMBER, PLAYERS_NUMBER
from Configuration.data_structure import *
from Components.maze_components import *
from Components.objects import *
from Components.subject import *

from random import randint

class World:
    def __init__(self, 
                 matrix: list[list[FieldRecord]]|None = None,
                 players: list[Player]|None = None,
                 clients: list[Client]|None = None,
                 destinations: list[Destination]|None = None,
                 walls: list[Wall]|None = None,
                 shelves: list[Shelf]|None = None) -> None:
        
        self.map = maps[MAP_INDEX]
        self.matrix = players,
        self.players=players,
        self.clients=clients
        self.destinations=destinations,
        self.walls=walls,
        self.shelves=shelves

    def choose_random_position() -> tuple[float, float]:

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

    def generate_new_world(self) -> None:
        
        players_id = 1
        clients_id = 1
        destinations_id = 1
        walls_id = 1
        shelves_id = 1

        y_range= len(self.map)
        x_range= len(self.map[0])

        for y in range (y_range):
            row=[]
            
            for x in range (x_range):
                    
                    character = self.map[y][x]
                    
                    if character == "#":
                        shelf = Shelf(x,y)
                        record=FieldRecord(shelves_id, entity_type.shelf, shelf, (x,y))
                        row.append([record])
                        self.shelves.append(shelf)
                        shelves_id += 1
                        
                    elif character == "!":
                        wall = Wall(x,y)
                        record=FieldRecord(walls_id, entity_type.wall, wall, (x,y))
                        row.append([record])
                        self.walls.append(wall)
                        walls_id += 1
                                        
                    elif character == "X":
                        destination = Destination(x,y)
                        record=FieldRecord(destinations_id, entity_type.destination, destination, (x,y))
                        row.append([record])
                        self.destinations.append(destination)
                        destinations_id += 1
                    
                    else:
                        row.append([])
            
            self.matrix.append(row)
                        
            for new_client in CLIENTS_NUMBER:
                
                position = self.choose_random_position()
                while self.is_empty(position) == False:
                    position = self.choose_random_position()
                new_client = Client(position[0], position[1])
                
                record=FieldRecord(clients_id, entity_type.client, new_client, (position[0], position[1]))
                self.clients.append(new_client)
                self.matrix[position[1]][position[0]] = [record]
                clients_id += 1
                
            
            for new_player in PLAYERS_NUMBER:
                
                position = self.choose_random_position()
                while self.is_empty(position) == False:
                    position = self.choose_random_position()
                new_player = Player(position[0], position[1])
                self.players.append([(position[0], position[1]), new_player])

                record=FieldRecord(players_id, entity_type.player, new_player, (position[0], position[1]))
                self.matrix[position[1]][position[0]] = [record]

    def add_component(self, new_coordinate: tuple[float, float], field: FieldRecord) -> None:

        if self.matrix is not None:
            self.matrix[new_coordinate[1]][new_coordinate[0]].append(field)

    def remove_component(self, old_coordinate: tuple[float, float], field: FieldRecord) -> None:

        if self.matrix is not None:
            self.matrix[old_coordinate[1]][old_coordinate[0]].remove(field)