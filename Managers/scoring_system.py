
from Configuration.setup import REWARD_CORRECT_DROP, MALUS_TRAVEL,MALUS_WRONG_DROP, BONUS_TRAVEL_NEW_CELL, MALUS_COLLISION

class ScoringSystem:
    def __init__(self):
        self.score = 0

    def add_points(self, points: int) -> None:
        self.score += points

    def add_reward_for_correct_drop(self) -> None:
        self.add_points(REWARD_CORRECT_DROP)

    def add_penalty_for_wrong_drop(self) -> None:
        self.add_points(MALUS_WRONG_DROP)

    def add_bonus_for_new_cell(self) -> None:
        self.add_points(BONUS_TRAVEL_NEW_CELL)

    def add_penalty_for_travel(self) -> None:
        self.add_points(MALUS_TRAVEL)
        
    def get_score(self) -> int:
        return self.score
    
    def reset_score(self) -> None:
        self.score = 0

    def add_penalty_for_collision(self) -> None:
        self.add_points(MALUS_COLLISION)