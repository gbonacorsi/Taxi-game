from random import randint

from Configuration.setup import MAP_INDEX, CLIENTS_NUMBER, PLAYERS_NUMBER
from Configuration.data_structure import ComponentRecord, entity_type
from Components.maze_components import Wall, Shelf
from Components.objects import Destination
from Components.subject import Player, Client
from Asset.levels import maps
from Utils.matrix_system import Matrix

class World:
    def __init__(self) -> None:
        
        self.map = maps[MAP_INDEX]
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
        
        return (x,y)

    def generate_random_components(self, number: int, component_type: entity_type) -> None:

        i = 0
        while i < number:
            
            
            position = self.choose_random_position()
            while self.matrix.is_empty(position) == False:
                position = self.choose_random_position()
            
            if component_type == entity_type.player:
                new_player = Player(self.players_id, (position[0], position[1]))
                record=ComponentRecord(self.players_id, entity_type.player, new_player)
                self.players.append(record)
                self.matrix.add_record(position,record)
                self.players_id += 1

            elif component_type == entity_type.client:
                new_client = Client(self.clients_id, (position[0], position[1]))
                record=ComponentRecord(self.clients_id, entity_type.client, new_client)
                self.clients.append(record)
                self.matrix.add_record(position,record)
                self.clients_id += 1

            elif component_type == entity_type.destination:
                new_destination = Destination(self.destinations_id, (position[0], position[1]))
                record=ComponentRecord(self.destinations_id, entity_type.destination, new_destination)
                self.destinations.append(record)
                self.matrix.add_record(position,record)
                self.destinations_id += 1
            
            i +=1

    def generate_new_world(self) -> None:

        self.map = maps[MAP_INDEX]
        y_range= len(self.map)
        x_range= len(self.map[0])

        for y in range (y_range):            
            for x in range (x_range):
                    
                    character = self.map[y][x]
                    
                    if character == "#":
                        shelf = Shelf(self.shelves_id, (x, y))
                        record=ComponentRecord(self.shelves_id, entity_type.shelf, shelf)
                        self.matrix.add_record((x,y),record)
                        self.shelves.append(record)
                        self.shelves_id += 1
                        
                    elif character == "!":
                        wall = Wall(self.walls_id, (x, y))
                        record=ComponentRecord(self.walls_id, entity_type.wall, wall)
                        self.matrix.add_record((x,y),record)
                        self.walls.append(record)
                        self.walls_id += 1                                    
                   
        self.generate_random_components(CLIENTS_NUMBER, entity_type.client)
        self.generate_random_components(PLAYERS_NUMBER, entity_type.player)
        self.generate_random_components(CLIENTS_NUMBER, entity_type.destination)

    def reset(self) -> None:

        self.matrix = Matrix(len(maps[MAP_INDEX]), len(maps[MAP_INDEX][0]))
        self.players: list[ComponentRecord] = []
        self.clients: list[ComponentRecord] = []
        self.destinations: list[ComponentRecord] = []
        self.walls: list[ComponentRecord] = []
        self.shelves: list[ComponentRecord] = []
        self.players_id = 1
        self.clients_id = 1
        self.destinations_id = 1
        self.walls_id = 1
        self.shelves_id = 1
        self.generate_new_world()