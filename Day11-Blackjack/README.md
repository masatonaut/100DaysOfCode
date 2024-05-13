# Python Blackjack Game

This Python script simulates a game of Blackjack, providing a console-based interface for users to play against an automated dealer. The game adheres to simplified Blackjack rules and is designed to be an engaging way to practice and understand the basic mechanics of Blackjack.

### Introduction

The Python Blackjack Game is an interactive script that allows users to experience the popular casino card game directly from the command line. It features various difficulty levels and a simple set of house rules to make the game accessible to beginners as well as challenging for more experienced players.

### Features

- **Various Difficulty Levels**: Users can choose the difficulty level by following specific hints to complete the project, ranging from Normal to Expert.
- **Simplified House Rules**: The game uses a simplified model of Blackjack, with an unlimited deck of cards and no removal of cards after they are drawn.
- **Interactive Gameplay**: Players can draw cards, see their scores, and compare them with the dealer's hand in real time.
- **ASCII Art Logo**: An ASCII art logo is displayed at the start of the game for visual appeal.
- **Clear Screen Functionality**: Utilizes the `os` module to clear the screen between games, ensuring a clean user interface.

### How to Use

1. **Starting the Game**: Run the Python script `art.py` in your preferred Python environment. Ensure Python is installed on your system.
2. **Playing the Game**: Follow the on-screen prompts to draw cards or hold your hand against the dealer.
3. **Game End and Restart**: Decide after each game whether to play another round or exit.

### Game Mechanics

- **deal_card() Function**: Randomly selects a card from the deck.
- **calculate_score() Function**: Calculates the score of a hand, taking into account the special role of the ace card.
- **compare() Function**: Compares the final scores of the player and the dealer to determine the outcome.

### Setup

To set up the Python Blackjack Game on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure `art.py` and the main game script are in the same directory.
2. **Run the Script**: Execute the main game script using a Python interpreter.
3. **Follow On-Screen Instructions**: Play Blackjack by following the in-game prompts.

### Dependencies

- Python 3.x
- The `random` module for card drawing
- The `os` module for screen clearing functionalities
