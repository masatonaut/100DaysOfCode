## Turtle Crossing Game

This Python script simulates a Turtle Crossing game, providing an interactive interface where the player controls a turtle to cross a busy road while avoiding cars. The game features real-time graphics and dynamic gameplay using the Turtle graphics library.

### Introduction

The Turtle Crossing Game is an engaging way to experience a classic arcade-style game. Players control a turtle character, navigating it across the screen to reach the finish line while avoiding oncoming cars. The game increases in difficulty with each successful crossing.

### Features

- **Real-Time Graphics**: Utilizes the Turtle graphics library to provide a visually appealing and interactive gameplay experience.
- **Dynamic Gameplay**: Cars appear at random intervals and speeds, increasing the game's challenge.
- **Score Tracking**: A scoreboard keeps track of the player's progress and levels.
- **Game Over Screen**: Displays a game over message when the turtle collides with a car.

### How to Use

1. **Starting the Game**: Run the script in your Python environment. Ensure Python and the Turtle graphics library are installed on your system.
2. **Playing the Game**: Use the `Up` arrow key to move the turtle up the screen. Avoid cars and reach the finish line to advance to the next level.
3. **Game End and Restart**: The game ends if the turtle collides with a car. Restart the game by running the script again.

### Game Mechanics

- **Player Class**: Manages the turtle's movement and position.
- **CarManager Class**: Controls car creation, movement, and collision detection.
- **Scoreboard Class**: Tracks and displays the player's score and level.

### Setup

To set up the Turtle Crossing Game on your local machine, follow these steps:

1. **Ensure Dependencies are Installed**: Ensure Python and the Turtle graphics library are installed. If not, install them using the following commands:
   ```bash
   pip install PythonTurtle
   ```
2. **Download the Game Files**: Ensure `player.py`, `car_manager.py`, and `scoreboard.py` are in the same directory as the main game script.
3. **Run the Script**: Execute the main game script using a Python interpreter:
   ```bash
   python main.py
   ```
4. **Follow On-Screen Instructions**: Play the game by following the in-game prompts and using the `Up` arrow key to move the turtle.

### Dependencies

- Python 3.x
- Turtle graphics library (often included with Python)
