# Higher or Lower Game

This is a Python implementation of a simple "Higher or Lower" game where players compare the number of followers of two random social media accounts. The player must guess which account has more followers. The game continues until the player makes an incorrect guess.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Play](#how-to-play)
- [Code Explanation](#code-explanation)
  - [Functions](#functions)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

The "Higher or Lower" game selects two random social media accounts from a predefined dataset and asks the player to guess which one has more followers. The game keeps track of the player's score and continues until an incorrect guess is made.

## Features

- Random selection of social media accounts.
- User-friendly display of account details.
- Real-time score tracking.
- Clear and restart the game screen after each guess.

## Setup

To set up and run the game on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure the script and any associated files (`logo`, `vs`, `data`) are in the same directory.
2. **Install Required Libraries**:
   Ensure you have the `art` library installed. You can install it via pip:
   ```sh
   pip install art
   ```
3. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

## How to Play

1. The game displays two social media accounts with their details.
2. The player is prompted to guess which account has more followers by typing 'A' or 'B'.
3. The game clears the screen and displays whether the guess was correct, updates the score, and presents the next comparison.
4. The game ends when the player makes an incorrect guess, displaying the final score.

## Code Explanation

### Functions

#### `get_random_account()`

Returns a random social media account from the `data` list.

#### `format_data(account)`

Formats the account data into a printable string showing the name, description, and country.

#### `check_answer(guess, a_followers, b_followers)`

Checks the user's guess against the actual follower counts. Returns `True` if the guess is correct and `False` otherwise.

#### `game()`

The main function that runs the game:

- Displays the logo.
- Initializes the score and game continuation flag.
- Retrieves two random accounts.
- Loops to prompt the user for guesses, update the score, and fetch new accounts until an incorrect guess is made.

## Dependencies

- Python 3.x
- `art` library

## Conclusion

This "Higher or Lower" game provides an engaging way to practice Python programming, particularly in using functions, handling user input, and working with data structures. The game can be further expanded by adding more features or integrating with real social media APIs for dynamic data. Enjoy playing and improving your Python skills!
