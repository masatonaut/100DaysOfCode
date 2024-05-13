# Python Number Guessing Game

This Python script offers a fun and engaging number guessing game through the command line. Players guess a randomly generated number within a certain range, with options for different difficulty levels affecting the number of allowed guesses.

### Introduction

The Python Number Guessing Game challenges players to guess a secret number between 1 and 100. The game is simple to understand but can be difficult to master, especially on harder difficulty settings. It provides a great way to practice logical thinking and basic programming concepts.

### Features

- **Difficulty Levels**: Players can choose between 'easy' and 'hard' difficulty levels, which determines the number of guesses they receive.
- **Interactive Gameplay**: The game provides feedback on each guess, informing the player if their guess was too high or too low.
- **ASCII Art Logo**: Displays an ASCII art logo at the start of the game for an engaging visual touch.
- **Immediate Feedback**: Players receive immediate feedback on their guesses and are informed when they run out of turns.

### How to Use

1. **Starting the Game**: Run the Python script containing the game code in your preferred Python environment.
2. **Choosing Difficulty**: Select your difficulty level at the start of the game.
3. **Making Guesses**: Enter your guesses based on the game's feedback and try to find the correct number within the limited number of turns.

### Game Mechanics

- **check_answer() Function**: Compares the player's guess to the secret number and returns the remaining number of guesses.
- **set_difficulty() Function**: Sets the number of turns based on the chosen difficulty level.
- **game() Function**: Handles the main game loop, including receiving user input and determining if the game continues or ends.

### Setup

To set up the Python Number Guessing Game on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure the script and any associated files (like `art.py` for the logo) are in the same directory.
2. **Run the Script**: Execute the game script using a Python interpreter.
3. **Follow On-Screen Instructions**: Play the game by following the prompts to guess the number.

### Dependencies

- Python 3.x
- The `random` module for generating random numbers
- An optional `art.py` file if using a logo for aesthetic enhancement
