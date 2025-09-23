from elements import Player, Client, Destination
from view import ScoreDisplay, DistanceDisplay
from utils import shelfs_coordinates

# Game setup
REWARD_CORRECT_DROP = 120
MALUS_TRAVEL = -1
MALUS_WRONG_DROP = -20

# Definition actions

class GameChart:
    
    def __init__(self, player: Player, client: Client, destination: Destination, score_display: ScoreDisplay, distance_display: DistanceDisplay) -> None:
        self.actions = {
            0: "go_up",
            1: "go_down",
            2: "go_left",
            3: "go_right",
            4: "client_picking",
            5: "client_dropping"
        }
        self.actions_mapping = {
            0: self.go_up,
            1: self.go_down,
            2: self.go_left,
            3: self.go_right,
            4: self.client_picking,
            5: self.client_dropping
        }

        self.player = player
        self.destination = destination
        self.client = client
        self.total_reward = 0
        self.picked_client = False
        self.drop_destination = False
        self.score_display = score_display
        self.distance_display = distance_display
        self.distance_client = 0
        self.distance_destination = 0

    def update_display(self) -> None:
        
        self.score_display.update_score(self.total_reward)
        self.distance_display.update_distance(self.distance_client, self.distance_destination)

    def calcule_move_reward_and_distance(self) -> None:

        self.total_reward += MALUS_TRAVEL
        self.distance_client = self.player.distance(self.client)
        self.distance_destination = self.client.distance(self.destination)
            
        self.update_display()
        
    def go_up(self) -> None:

        if not self.picked_client:
            self.player.go_up(self.client, self.destination)
        elif self.picked_client:
            self.player.go_up(self.client, self.destination)
            self.client.go_up(self.destination)

        self.calcule_move_reward_and_distance()

    def go_down(self) -> None:
  
        if not self.picked_client:
            self.player.go_down(self.client, self.destination)
        elif self.picked_client:
            self.player.go_down(self.client, self.destination)
            self.client.go_down(self.destination)

        self.calcule_move_reward_and_distance()

    def go_left(self):

        if not self.picked_client:
            self.player.go_left(self.client, self.destination)
        elif self.picked_client:
            self.player.go_left(self.client, self.destination)
            self.client.go_left(self.destination)

        self.calcule_move_reward_and_distance()

    def go_right(self):

        if not self.picked_client:
            self.player.go_right(self.client, self.destination)
        elif self.picked_client:
            self.player.go_right(self.client, self.destination)
            self.client.go_right(self.destination)

        self.calcule_move_reward_and_distance()

    def client_picking(self):

        if self.player.distance(self.client) == 0:
            self.picked_client = True

    def client_dropping(self):
        
        if self.picked_client and self.client.distance(self.destination) == 0:
            self.picked_client = False
            self.drop_destination = True
            self.total_reward += REWARD_CORRECT_DROP
            self.score_display.update_score(self.total_reward)
            
        if self.picked_client and self.player.distance(self.destination) != 0:
            self.picked_client = False
            self.drop_destination = True
            self.total_reward += MALUS_WRONG_DROP
            self.score_display.update_score(self.total_reward)
