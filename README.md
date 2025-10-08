# 🚕 Taxi Game - Advanced Reinforcement Learning Environment

A sophisticated agent pickup and delivery simulation built with Python and Turtle Graphics, featuring a modular Entity-Component-System architecture designed for both interactive gameplay and advanced AI training scenarios.

## ✨ Key Features

- **🎮 Interactive Gameplay**: Smooth keyboard controls with real-time feedback
- **🤖 AI Training Platform**: Full reinforcement learning integration server with customizable reward systems
- **🏗️ Modular Architecture**: Professional-grade Entity-Component-System design with clean separation of concerns
- **🎯 Dynamic Scoring**: Intelligent scoring system with configurable penalties and rewards
- **🎨 Rich Graphics**: Turtle-based rendering with animation support and visual effects
- **🔧 Configuration System**: Flexible settings management with environment-specific configs

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+ (recommended: Python 3.10+)
pip (Python package manager)
```

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/gbonacorsi/Taxi-game.git
cd "Taxi game"

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

```

## 🎯 Gameplay Guide

### Controls
- **Arrow Keys** (↑↓←→) - Navigate the taxi through the environment
- **Pick** (P) - Press P to pick
- **Drop** (D) - Press D to drop

### Game Mechanics
- **Movement Cost**: Each move incurs a small penalty to encourage efficiency
- **Successful Pickup**: Positive reward for collecting passengers
- **Correct Delivery**: Major reward bonus for delivering to correct destination
- **Wrong Delivery**: Penalty for incorrect drop-offs

### Objective
Guide your agent (represented by a distinctive sprite) to efficiently pick up passengers and deliver them to their designated destinations while maximizing your cumulative score and minimizing travel time.

## 📁 Project Architecture

```
Taxi Game/
├── main.py                    # Application entry point and initialization
├── requirements.txt          # Python dependencies and versions
├── LICENSE                   # Project license (MIT)
├── README.md                # This documentation
│
├── AI/                       # Artificial Intelligence modules
│   └── (RL algorithms and training scripts)
│
├── Asset/                    # Game assets and data definitions
│   ├── labels.py            # UI text and label constants
│   └── levels.py            # Level definitions and configurations
│
├── Components/               # ECS Component definitions
│   ├── maze_components.py      # Maze-specific game components
│   ├── subjects_components.py   # Player and client game components
│   └── objects_components.py   # Destination game components
│
├── Configuration/            # Settings and configuration management
│   ├── data_structure.py   # Structure of the data exchange on the game
│   └── setup.py            # Game setup and initialization
│
├── Core/                     # Core game engine functionality
│   ├── engine.py            # Main game engine and loop management
│   ├── game_manager.py      # Coordinate the event based on the keyboard/interface triggers
│   ├── event_manager.py      # Coordinate game components and rendering
│   ├── state_manager.py      # Manage the components state across the game
│   └── loop.py              # Game loop implementation
│
├── Entities/                 # Game entity definitions
│   └── maze_entities.py     # Maze and environment entities
│   ├── subjects_entities.py   # Player and client game entities
│   └── objects_entities.py   # Destination game entities
│
├── Managers/                 # System managers and controllers
│   ├── collision_system.py  # Collision detection and handling
│   ├── inventory_system.py  # Picking and dropping management
│   ├── scoring_system.py    # Reward calculation
│   ├── validation_system.py  # Validation correct actions
│   ├── word_manager.py      # Simulation matrix management
│   └── movement_system.py   # Movement mechanics and validation
│
├── Network/                  # Networking capabilities (future)
│   ├── client/              # Client-side networking - Design to run in separate environement
│   └── server/              # Server-side networking
│
├── Presentation/             # Rendering and display systems
│   ├── Turle                # Display with Turtle rending system
│   ├──── display_system.py    # Display management and UI
│   ├──── render_system.py     # Graphics rendering pipeline
│   └──── ui_system.py         # User interface components
│
├── Systems/                  # Game logic systems
│   └── Input_management.py  # Input keyboard handling and event processing
│
└── Utils/                     # Utility functions and helpers
    ├── matrix_system.py        # Coordinate system and spatial utilities
    └── expetion_system.py        # Custom errors
```

### Advanced Training Features
- **Custom Reward Functions**: Define domain-specific reward structures
- **State Space Configuration**: Flexible observation space definitions
- **Action Space Customization**: Discrete and continuous action support
- **Multi-Agent Support**: Concurrent taxi operations
- **Curriculum Learning**: Progressive difficulty scaling

## � Configuration & Customization

### Game Settings
The game supports extensive customization through configuration files:

```python
# Configuration/setup.py

# GAME SETTINGS
MAP_INDEX = 0
PLAYERS_NUMBER = 2     # when Input_Type = KEYBOARD -> max 5 players
CLIENTS_NUMBER = 1
INPUT_TYPE = input_type.SERVER    
RENDERING = True
RENDER_ENGINE = "Turtle" 

```

## 📧 Contact & Credits

**Project Creator and Maintainer**: Giorgio Bonacorsi  
**Repository**: [https://github.com/gbonacorsi/Taxi-game](https://github.com/gbonacorsi/Taxi-game)  
**License**: MIT License

### Acknowledgments
- Built with Python's robust ecosystem
- Inspired by classic taxi dispatch optimization problems
- Designed for reinforcement learning research and education
- Community-driven development and continuous improvement

---

*Happy coding and training! 🚕🤖*