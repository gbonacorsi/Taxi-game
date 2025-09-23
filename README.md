# Taxi Game - Reinforcement Learning Environment

A taxi pickup and delivery game built with Python Turtle Graphics, designed for both manual play and AI training.

## 🎮 Features

- **Interactive Gameplay**: Manual control with keyboard
- **AI Training Ready**: Compatible with reinforcement learning algorithms
- **Modular Design**: Clean separation of game logic, graphics, and AI
- **Real-time Scoring**: Dynamic scoring system with penalties and rewards
- **Visual Effects**: Blinking animations and smooth graphics

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/taxi-game-rl.git
cd taxi-game-rl

# Run the game
python main.py
```

## 🎯 How to Play

### Controls
- **W/A/S/D** or **Arrow Keys** - Move the taxi
- **E** - Pick up client (when near)
- **Q** - Drop off client (at destination)

### Scoring System
- **Movement**: -1 point per move
- **Correct Delivery**: +120 points
- **Wrong Delivery**: -20 points

### Objective
Navigate the taxi (gold square) to pick up clients (yellow circle) and deliver them to their destinations (orange circle) while maximizing your score.

## 📁 Project Structure

```
taxi-project/
├── main.py              # Main game entry point
├── elements.py          # Game objects (Player, Client, Destination)
├── environement.py      # Environment and maze setup
├── view.py             # Display and rendering logic
├── rules.py            # Game rules and logic (GameChart)
├── levels.py           # Level definitions
├── utils.py            # Utility functions
├── constants.py        # Game constants and configuration
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore rules
└── tests/             # Unit tests (coming soon)
```

## 🤖 AI Training

The game is designed to be compatible with reinforcement learning frameworks:

```python
from rules import GameChart
from elements import Player, Client, Destination

# Initialize environment
player = Player()
client = Client()
destination = Destination()
game = GameChart(player, client, destination, score_display)

# Example RL integration
state = game.get_state()
action = agent.choose_action(state)
reward = game.step(action)
```

## 🛠️ Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Write descriptive variable names
- Add docstrings to functions and classes

### Testing
```bash
# Run tests (when implemented)
python -m pytest tests/
```

## 📈 Performance Metrics

Track your gameplay:
- High scores
- Average delivery time
- Success rate
- Movement efficiency

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python Turtle Graphics
- Inspired by classic taxi dispatch problems
- Designed for reinforcement learning research

## 📧 Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/taxi-game-rl](https://github.com/yourusername/taxi-game-rl)