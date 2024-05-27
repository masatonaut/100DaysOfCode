# Turtle Race Program

This is a Python implementation of a turtle race simulator using the Turtle graphics module. The program allows users to bet on which turtle will win the race and then simulates the race.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
  - [Setup](#setup)
  - [Race Logic](#race-logic)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This program simulates a turtle race where users can place a bet on a turtle of their chosen color. The turtles then race across the screen, and the program declares the winner, comparing it with the user's bet.

## Features

- User input for betting on a turtle.
- Six different colored turtles to bet on.
- Randomized turtle movement to simulate the race.
- Displays the winning turtle and checks it against the user's bet.

## Setup

To set up and run the turtle race program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py` file.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

````

## How to Use

1. Run the program.
2. A prompt will appear asking you to bet on which turtle will win the race. Enter a color (red, orange, yellow, green, blue, purple).
3. The race will start automatically if a bet is placed.
4. Watch the turtles race across the screen.
5. The program will announce the winning turtle and whether your bet was correct.
6. Click on the Turtle graphics window to close it.

## Code Explanation

### Setup

The program initializes the screen and sets up the six turtles with different colors and starting positions.

```python
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
```

### Race Logic

The race starts if a bet is placed. Each turtle moves forward by a random distance until one crosses the finish line. The program then checks if the winning turtle matches the user's bet.

```python
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
```

## Dependencies

- Python 3.x
- `turtle` module (usually included with Python)

Ensure that `main.py` is in the same directory where you run the script.

## Conclusion

The turtle race program provides an interactive and fun way to simulate a race using the Turtle graphics module. It demonstrates basic user input handling, random movement, and graphical output. Enjoy the race and may the best turtle win!
````
