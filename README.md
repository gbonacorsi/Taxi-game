# 🚕 Taxi Game - Advanced Reinforcement Learning Environment

A sophisticated taxi pickup and delivery simulation built with Python and Turtle Graphics, featuring a modular Entity-Component-System architecture designed for both interactive gameplay and advanced AI training scenarios.

## ✨ Key Features

- **🎮 Interactive Gameplay**: Smooth keyboard controls with real-time feedback
- **🤖 AI Training Platform**: Full reinforcement learning integration with customizable reward systems
- **🏗️ Modular Architecture**: Professional-grade Entity-Component-System design with clean separation of concerns
- **🎯 Dynamic Scoring**: Intelligent scoring system with configurable penalties and rewards
- **🎨 Rich Graphics**: Turtle-based rendering with animation support and visual effects
- **🧪 Testing Framework**: Comprehensive test suite with pytest integration
- **📊 Performance Analytics**: Built-in metrics tracking and game state analysis
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
- **WASD** - Alternative movement controls
- **Space** - Interact (pick up passengers, drop off at destinations)
- **R** - Reset current level
- **ESC** - Pause/Menu

### Game Mechanics
- **Movement Cost**: Each move incurs a small penalty to encourage efficiency
- **Successful Pickup**: Positive reward for collecting passengers
- **Correct Delivery**: Major reward bonus for delivering to correct destination
- **Wrong Delivery**: Penalty for incorrect drop-offs
- **Time Bonus**: Additional rewards for fast completions

### Objective
Guide your taxi (represented by a distinctive sprite) to efficiently pick up passengers and deliver them to their designated destinations while maximizing your cumulative score and minimizing travel time.

## 📁 Project Architecture

```
Taxi Game/
├── main.py                    # Application entry point and initialization
├── main_clean.py             # Cleaned production version
├── requirements.txt          # Python dependencies and versions
├── LICENSE                   # Project license (MIT)
├── README.md                # This documentation
├── Architectural notes.xlsx  # Design documentation and notes
│
├── AI/                       # Artificial Intelligence modules
│   └── (RL algorithms and training scripts)
│
├── Asset/                    # Game assets and data definitions
│   ├── labels.py            # UI text and label constants
│   └── levels.py            # Level definitions and configurations
│
├── Components/               # ECS Component definitions
│   └── maze_components.py   # Maze-specific game components
│
├── Configuration/            # Settings and configuration management
│   └── setup.py            # Game setup and initialization
│
├── Core/                     # Core game engine functionality
│   ├── Engine.py            # Main game engine and loop management
│   └── Loop.py              # Game loop implementation
│
├── Entities/                 # Game entity definitions
│   └── maze_entities.py     # Maze and environment entities
│
├── Managers/                 # System managers and controllers
│   ├── collision_system.py  # Collision detection and handling
│   ├── level_system.py      # Level management and progression
│   └── movement_system.py   # Movement mechanics and validation
│
├── Network/                  # Networking capabilities (future)
│   ├── client/              # Client-side networking
│   └── server/              # Server-side networking
│
├── Presentation/             # Rendering and display systems
│   ├── display_system.py    # Display management and UI
│   ├── render_system.py     # Graphics rendering pipeline
│   └── ui_system.py         # User interface components
│
├── Systems/                  # Game logic systems
│   └── Input_management.py  # Input handling and event processing
│
└── Utils/                    # Utility functions and helpers
    └── coordinate.py        # Coordinate system and spatial utilities
```

## 🤖 AI Integration & Training

The game provides a comprehensive reinforcement learning environment with multiple integration points:

### Basic RL Integration
```python
from Core.Engine import Engine
from AI.rl_interface import RLEnvironment

# Initialize RL environment
env = RLEnvironment()
state = env.reset()

# Training loop
for episode in range(1000):
    action = agent.select_action(state)
    next_state, reward, done, info = env.step(action)
    agent.learn(state, action, reward, next_state, done)
    state = next_state
    
    if done:
        state = env.reset()
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
GAME_CONFIG = {
    "grid_size": (10, 10),
    "taxi_speed": 1,
    "reward_pickup": 10,
    "reward_delivery": 100,
    "penalty_move": -1,
    "penalty_wrong_delivery": -20
}
```

### Level Design
Create custom levels with varying complexity:
- **Static Obstacles**: Walls and barriers
- **Dynamic Elements**: Moving obstacles and time-based challenges
- **Multiple Passengers**: Concurrent pickup/delivery scenarios
- **Special Zones**: Speed boosts, penalty areas, bonus regions

## 🧪 Testing & Quality Assurance

### Test Coverage
```bash
# Run full test suite
pytest tests/ --cov=. --cov-report=html

# Run specific test categories
pytest tests/test_components.py -v
pytest tests/test_systems.py -v
pytest tests/test_integration.py -v
```

### Performance Benchmarks
- **Frame Rate**: Target 60 FPS for smooth gameplay
- **Memory Usage**: Optimized for minimal memory footprint
- **AI Training Speed**: Configurable simulation speeds for training

## 📊 Analytics & Metrics

### Built-in Metrics
- **Episode Statistics**: Steps, rewards, completion time
- **Performance Tracking**: Success rates, efficiency scores
- **AI Training Metrics**: Learning curves, convergence analysis
- **System Performance**: FPS, memory usage, processing time

### Data Export
```python
# Export training data
metrics = game.get_episode_metrics()
metrics.export_to_csv("training_data.csv")
metrics.export_to_json("episode_summary.json")
```

## 🚀 Advanced Features

### Multi-Agent Support
```python
# Initialize multiple taxis
env = MultiTaxiEnvironment(num_taxis=3)
states = env.reset()

# Coordinated AI training
for taxi_id, state in enumerate(states):
    action = agents[taxi_id].select_action(state)
    next_states, rewards, dones, info = env.step(actions)
```

### Custom Rendering Backends
- **Turtle Graphics**: Default lightweight renderer
- **Pygame Integration**: Enhanced graphics and performance
- **Headless Mode**: Fast simulation without visual output
- **Web Interface**: Browser-based visualization (planned)

## 🛠️ Development Guidelines

### Code Standards
- **PEP 8 Compliance**: Consistent code formatting
- **Type Hints**: Full type annotation coverage
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Robust exception management
- **Logging**: Structured logging throughout the application

### Architecture Principles
- **Single Responsibility**: Each module has a clear, focused purpose
- **Dependency Injection**: Loose coupling between components
- **Event-Driven Design**: Asynchronous communication between systems
- **Testability**: All components designed for unit testing

### Contributing Workflow
1. **Fork & Clone**: Create your development environment
2. **Feature Branch**: `git checkout -b feature/your-feature-name`
3. **Test Coverage**: Ensure all new code has tests
4. **Code Review**: Submit PR with detailed description
5. **Documentation**: Update relevant documentation

## 🔍 Troubleshooting

### Common Issues
**Import Errors**: Ensure all dependencies are installed and PYTHONPATH is configured
```bash
pip install -r requirements.txt
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Graphics Issues**: Verify turtle graphics compatibility
```python
import turtle
turtle.setup(800, 600)  # Test basic turtle functionality
```

**Performance Issues**: Enable headless mode for training
```python
env = TaxiEnvironment(render_mode="headless")
```

### Debug Mode
```bash
# Run with debug logging
python main.py --debug --log-level DEBUG

# Profile performance
python -m cProfile main.py > performance.prof
```

## 📈 Roadmap & Future Development

### Planned Features
- **🌐 Web Interface**: Browser-based game client
- **🔗 REST API**: HTTP interface for external integrations
- **📱 Mobile Support**: Touch-based controls for mobile devices
- **🎵 Audio System**: Sound effects and background music
- **🏆 Leaderboards**: Global and local high score tracking
- **🔄 Save System**: Game state persistence and loading

### Research Applications
- **Multi-Agent RL**: Cooperative and competitive scenarios
- **Transfer Learning**: Cross-domain knowledge transfer
- **Curriculum Learning**: Adaptive difficulty progression
- **Human-AI Interaction**: Mixed human-AI gameplay

## 📝 License & Attribution

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### Dependencies
- **Python Turtle**: Built-in graphics library
- **NumPy**: Numerical computations (if used in AI modules)
- **Pytest**: Testing framework
- **Additional packages**: See requirements.txt for complete list

## 🤝 Community & Support

### Getting Help
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: General questions and community support
- **Wiki**: Detailed guides and tutorials (coming soon)

### Contributing
We welcome contributions! Areas where help is especially appreciated:
- **Documentation**: Improving guides and examples
- **Testing**: Expanding test coverage
- **AI Algorithms**: New RL implementations
- **Performance**: Optimization and profiling
- **Graphics**: Enhanced visual effects

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