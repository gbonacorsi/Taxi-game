"""
Taxi Game - Main Application Entry Point

A taxi pickup and delivery game built with Python Turtle Graphics.
Designed for both manual play and reinforcement learning training.
"""

import turtle
from typing import Optional

import environement as env
import elements as elm
import view as render
import Asset.levels as levels
from utils import choose_random_position
from elements import BLINK_COUNTER, BLINK_SPEED
from rules import GameChart


class TaxiGame:
    """Main game controller for the Taxi Game."""
    
    def __init__(self, width: int = 800, height: int = 800, level_index: int = 0, headless: bool = True):
        """Initialize the taxi game.
        
        Args:
            width: Screen width in pixels
            height: Screen height in pixels  
            level_index: Index of the level to load from levels.maps
            headless: If True, run without graphics for faster AI training
        """
        self.width = width
        self.height = height
        self.level_index = level_index
        self.blink_counter = 0
        self.headless = headless
        
        # Initialize screen only if not headless
        if not self.headless:
            self._setup_screen()
        
        # Initialize game objects
        self._create_game_objects()
        
        # Initialize game chart (rules and state)
        self.game_chart = GameChart(
            self.player, 
            self.client, 
            self.destination, 
            self.score_display if not self.headless else None,
            self.distance_display if not self.headless else None
        )
        
        # Setup display only if not headless

        self._setup_display()
        self._setup_controls()

            # Just place objects without rendering
        self._respawn_objectives()
    
    def _setup_screen(self) -> None:
        """Initialize the turtle screen with game settings."""
        if self.headless:
            return  # Skip screen setup in headless mode
            
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Taxi Game")
        self.screen.setup(width=self.width, height=self.height)
        self.screen.tracer(0)  # Turn off animation for better performance
    
    def _create_game_objects(self) -> None:
        """Create all game objects (pen, player, client, destination, displays)."""
        self.pen = env.Pen()
        self.player = elm.Player()
        self.client = elm.Client()
        self.destination = elm.Destination()
        self.text_display = render.TextDisplay()
        self.score_display = render.ScoreDisplay()
        self.distance_display = render.DistanceDisplay()
        self.current_map = levels.maps[self.level_index]
        
        # Hide turtle cursors for cleaner display
        self.pen.hideturtle()
        self.player.hideturtle()
        self.client.hideturtle()
        self.destination.hideturtle()
    
    def _setup_display(self) -> None:
        """Setup the maze and initial positions."""
        if self.headless:
            # Skip rendering in headless mode
            self._respawn_objectives()
            return
            
        render.setup_maze(
            self.text_display,
            self.score_display, 
            self.distance_display,
            self.pen,
            self.current_map,
            self.player,
            self.client,
            self.destination,
            self.game_chart.total_reward
        )
        
        # Place client and destination at random positions
        self._respawn_objectives()
    
    def _respawn_objectives(self) -> None:
        """Place client and destination at new random positions."""
        client_position = choose_random_position()
        destination_position = choose_random_position()
        
        self.client.goto(client_position)
        self.destination.goto(destination_position)
    
    def _setup_controls(self) -> None:
        """Setup keyboard controls for the game."""
        turtle.listen()
        
        # Movement controls - WASD and Arrow keys
        turtle.onkey(self.game_chart.go_up, "w")
        turtle.onkey(self.game_chart.go_up, "Up")
        turtle.onkey(self.game_chart.go_down, "s")
        turtle.onkey(self.game_chart.go_down, "Down")
        turtle.onkey(self.game_chart.go_left, "a")
        turtle.onkey(self.game_chart.go_left, "Left")
        turtle.onkey(self.game_chart.go_right, "d")
        turtle.onkey(self.game_chart.go_right, "Right")
        
        # Action controls
        turtle.onkey(self.game_chart.client_picking, "e")
        turtle.onkey(self.game_chart.client_dropping, "q")
    
    def _update_blinking(self) -> None:
        """Handle the blinking animation for the client."""
        if self.headless:
            return  # Skip blinking in headless mode
            
        self.blink_counter += 1
        if self.blink_counter >= BLINK_SPEED:
            self.client.blink()
            self.blink_counter = 0
    
    def run(self) -> None:
        """Start the main game loop."""
        if not self.headless:
            print("🚕 Taxi Game Started!")
            print("Controls: WASD/Arrows to move, E to pick up, Q to drop off")
            print("Objective: Pick up clients (yellow) and deliver to destinations (orange)")
        
        try:
            while True:
                # Game round loop - continue until client is dropped off
                while not self.game_chart.drop_destination:
                    if not self.headless:
                        self.screen.update()
                        self._update_blinking()
                    # In headless mode, just continue without graphics updates
                
                # Round completed - respawn objectives for next round
                previous_mission_score = self.game_chart.total_reward
                self.game_chart.drop_destination = False
                self.game_chart.total_reward = 0
                
                if not self.headless:
                    print(f"🎯 Delivery completed! Score: {previous_mission_score}")
                self._respawn_objectives()
                
        except turtle.Terminator:
            if not self.headless:
                print("👋 Game closed by user")
        except KeyboardInterrupt:
            if not self.headless:
                print("👋 Game interrupted by user")
        finally:
            self._cleanup()
    
    def _cleanup(self) -> None:
        """Clean up resources when game ends."""
        if not self.headless:
            try:
                self.screen.bye()
            except:
                pass


def main():
    """Entry point for the taxi game application."""
    try:
        game = TaxiGame()
        game.run()
    except Exception as e:
        print(f"❌ Error starting game: {e}")
        print("Make sure all required modules are available and try again.")


if __name__ == "__main__":
    main()