from random import randint

from Configuration.setup import *
from Configuration.data_structure import *
from Components.maze_components import *
from Components.objects import *
from Components.subject import *
from Asset.levels import maps
from Utils.matrix_system import Matrix

class World:
    def __init__(self) -> None:
        
        #self.map = maps[MAP_INDEX]
        self.matrix = Matrix(len(maps[MAP_INDEX]), len(maps[MAP_INDEX][0]))
        self.players: list[ComponentRecord] | []= []
        self.clients: list[ComponentRecord] | []=[]
        self.destinations: list[ComponentRecord] | []=[]
        self.walls: list[ComponentRecord] | []=[]
        self.shelves: list[ComponentRecord] | []=[]
        self.players_id = 1
        self.clients_id = 1
        self.destinations_id = 1
        self.walls_id = 1
        self.shelves_id = 1

    def choose_random_position(self) -> dict:

        map_id=MAP_INDEX
        y = randint(0, len(maps[map_id]) - 1)
        x = randint(0, len(maps[map_id][y]) - 1)
        
        data={}
        data["x"] = x
        data["y"] = y
        
        return data

    def generate_random_components(self, id:int, number: int, component_type: entity_type) -> None:

        for i in range(number):
            
            position = self.choose_random_position()
            while self.is_empty(position) == False:
                position = self.choose_random_position()
            
            if component_type == entity_type.player:
                new_player = Player(self.players_id, position[0], position[1])
                record=ComponentRecord(self.players_id, entity_type.player, new_player, (position[0], position[1]))
                self.players.append(record)
                old_row_string = self.map[position[1]]
                list_row = list(old_row_string)
                list_row[position[0]] = "P"
                new_row_string = "".join(list_row)
                self.map[position[1]] = new_row_string
                self.players_id += 1

            elif component_type == entity_type.client:
                new_client = Client(self.clients_id, position[0], position[1])
                record=ComponentRecord(self.clients_id, entity_type.client, new_client, (position[0], position[1]))
                self.clients.append(record)
                self.matrix[position[1]][position[0]] = [record]
                
                old_row_string = self.map[position[1]]
                list_row = list(old_row_string)
                list_row[position[0]] = "C"
                new_row_string = "".join(list_row)
                self.map[position[1]] = new_row_string
                
                self.clients_id += 1

            elif component_type == entity_type.destination:
                new_destination = Destination(self.destinations_id, position[0], position[1])
                record=ComponentRecord(self.destinations_id, entity_type.destination, new_destination, (position[0], position[1]))
                self.destinations.append(record)
                self.matrix[position[1]][position[0]] = [record]
                old_row_string = self.map[position[1]]
                list_row = list(old_row_string)
                list_row[position[0]] = "X"
                new_row_string = "".join(list_row)
                self.map[position[1]] = new_row_string
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
                        record=ComponentRecord(self.shelves_id, entity_type.shelf, shelf, (x,y))
                        row.append([record])
                        self.shelves.append(shelf)
                        self.shelves_id += 1
                        
                    elif character == "!":
                        wall = Wall(self.walls_id, x, y)
                        record=ComponentRecord(self.walls_id, entity_type.wall, wall, (x,y))
                        row.append([record])
                        self.walls.append(wall)
                        self.walls_id += 1
                                        
                    else:
                        row.append([])
            
            self.matrix.append(row)
            
        self.generate_random_components(self.clients_id, CLIENTS_NUMBER, entity_type.client)
        self.generate_random_components(self.players_id, PLAYERS_NUMBER, entity_type.player)
        self.generate_random_components(self.destinations_id, CLIENTS_NUMBER, entity_type.destination)

    def reset(self) -> None:

        self.matrix = Matrix(len(maps[MAP_INDEX]), len(maps[MAP_INDEX][0]))
        self.players: list[ComponentRecord] | []= []
        self.clients: list[ComponentRecord] | []=[]
        self.destinations: list[ComponentRecord] | []=[]
        self.walls: list[ComponentRecord] | []=[]
        self.shelves: list[ComponentRecord] | []=[]
        self.players_id = 1
        self.clients_id = 1
        self.destinations_id = 1
        self.walls_id = 1
        self.shelves_id = 1
        self.generate_new_world()