import os, sys
from Entities.maze_entities import Maze, Shelf, Player, Client, Destination, Wall

class Display_game:
    
    def render(self, initial_coor: tuple = (-240, 180), map: list[list[str]] = [[]], square_interval: int = 24) -> None:
        y_range= len(map)
        x_range= len(map[0])
        
        player_list = []
        client_list = []
        destination_list = []
        wall_list = []
        shelf_list = []
        
        for y in range (y_range):
            for x in range (x_range):
                character = map[y][x]
                screen_x = initial_coor[0] + (x * square_interval)
                screen_y = initial_coor[1] - (y * square_interval)

                if character == "#":
                    shelf = Shelf()
                    shelf.goto(screen_x, screen_y)
                    shelf.stamp()
                    shelf_list.append(shelf)

                if character == "!":
                    wall = Wall()
                    wall.goto(screen_x, screen_y)
                    wall.stamp()
                    wall_list.append(wall)
                    
                if character == "P":
                    player = Player()
                    player.goto(screen_x, screen_y)
                    player.stamp()
                    player_list.append(player)
                    
                if character == "c":
                    client = Client()
                    client.goto(screen_x, screen_y)
                    client.stamp()
                    client_list.append(client)
                    
                if character == "X":
                    destination = Destination() 
                    destination.goto(screen_x, screen_y)
                    destination.stamp()
                    destination_list.append(destination)
                    
