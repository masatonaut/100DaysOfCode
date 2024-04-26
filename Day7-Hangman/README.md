## Hangman: A Python Game

This Python game invites players to guess letters in a secret word. The game continues until the player successfully discovers the word or runs out of lives. The program uses three separate files: `main.py`, `hangman_words.py`, and `hangman_art.py`, each containing essential components of the game.

### How to Play

Upon starting the game, you will see a random word represented by underscores for each letter. Your goal is to guess this word one letter at a time. If your guessed letter is in the word, it will appear in its correct position. If not, you will lose a life. The game ends either when you correctly guess the word or when you run out of lives.

### What You Need to Know

- **main.py**: Contains the game logic.
- **hangman_words.py**: Includes a list of words from which the game randomly selects.
- **hangman_art.py**: Provides ASCII art for the hangman graphics and the game's logo.

#### main.py

- Imports random word selection from `hangman_words.py` and ASCII art from `hangman_art.py`.
- Tracks the number of lives remaining and checks if the game has ended.

#### hangman_words.py

- Contains a list of words used in the game. These are challenging and uncommon words designed to make the game interesting.

#### hangman_art.py

- Stores stages of the hangman drawing depending on the player's remaining lives.
- Displays a logo at the beginning of the game.

### Setup

To set up the game on your local machine, follow these steps:

1. **Clone the repository or download the files**: Make sure all files are in the same directory.
2. **Run `main.py`**: This file will execute the game. Make sure Python is installed on your system.
3. **Start guessing**: Play the game by entering letters when prompted.

### Dependencies

- Python 3.x
- No external libraries required for running the base game.

Enjoy testing your word-guessing skills with this classic Hangman game implemented in Python! Feel free to modify the word list or the ASCII art to customize your gaming experience.
