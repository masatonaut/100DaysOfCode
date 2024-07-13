# Flask Number Guessing Game

This project is a simple web application built with Flask that allows users to guess a randomly generated number between 0 and 9.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/flask-number-guessing-game.git
   cd flask-number-guessing-game
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install Flask
   ```

## Usage

1. **Create the Python script (app.py):**

   ```python
   from flask import Flask
   import random

   random_number = random.randint(0, 9)
   print(random_number)

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "<h1>Guess a number between 0 and 9</h1>" \
              "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

   @app.route("/<int:guess>")
   def guess_number(guess):
       if guess > random_number:
           return "<h1 style='color: purple'>Too high, try again!</h1>" \
                  "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
       elif guess < random_number:
           return "<h1 style='color: red'>Too low, try again!</h1>"\
                  "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
       else:
           return "<h1 style='color: green'>You found me!</h1>" \
                  "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

   if __name__ == "__main__":
       app.run(debug=True)
   ```

2. **Run the application:**

   ```sh
   python app.py
   ```

3. **Access the application:**
   - Open your web browser and go to `http://127.0.0.1:5000/` to see the home page.
   - Go to `http://127.0.0.1:5000/<guess>` to guess a number between 0 and 9 (replace `<guess>` with your number).

## How It Works

- The application generates a random number between 0 and 9 when it starts.
- The home page (`/`) displays a message prompting the user to guess a number.
- When a user enters a guess in the URL (e.g., `/3`), the application responds with a message indicating whether the guess is too high, too low, or correct.
