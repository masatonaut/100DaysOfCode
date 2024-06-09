# U.S. States Game

This is a Python-based game for learning the names and locations of the U.S. states. The game prompts the user to enter the names of U.S. states, displays them on a map, and helps track which states the user has correctly identified. If the user chooses to exit the game, it generates a list of states the user needs to learn.

## Requirements

- Python 3.x
- `turtle` module (comes with the standard Python library)
- `pandas` module

You can install the `pandas` module using pip:

```
pip install pandas
```

## Files

- `main.py`: The main script that runs the game.
- `blank_states_img.gif`: The image file of the U.S. map used in the game.
- `50_states.csv`: A CSV file containing the names of the 50 states and their corresponding x and y coordinates on the map.

## How to Play

1. Run the `main.py` script.
2. A window with the U.S. map will appear.
3. Enter the name of a U.S. state when prompted.
4. If you guess correctly, the state name will appear on the map at its correct location.
5. The game continues until you have correctly guessed all 50 states or choose to exit.
6. If you enter "Exit", the game will save a list of states you have not yet guessed to a file named `states_to_learn.csv`.

## Code Explanation

### Import Libraries

```python
import turtle
import pandas
```

Imports the necessary libraries for the game.

### Set Up the Screen

```python
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
```

Sets up the game window and displays the U.S. map image.

### Load Data

```python
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
```

Loads the CSV file containing state names and coordinates, and initializes lists for all states and guessed states.

### Main Game Loop

```python
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
```

- Prompts the user to enter a state name.
- If the user enters "Exit", it saves the states not yet guessed to a CSV file and exits the loop.
- If the user guesses a state correctly, it adds the state to the guessed list and displays it on the map.

## Exiting the Game

- To exit the game, enter "Exit" when prompted.
- The game will generate a `states_to_learn.csv` file containing the names of states you have not yet guessed, so you can learn and practice them later.
