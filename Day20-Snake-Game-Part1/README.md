# Snake Game Program

This is a Python implementation of the classic Snake game using the Turtle graphics module. The program allows users to control the snake using the arrow keys, navigating it around the screen.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
  - [Screen Setup](#screen-setup)
  - [Snake Control](#snake-control)
  - [Game Loop](#game-loop)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This program is a simple implementation of the classic Snake game. The snake moves around the screen and can be controlled using the arrow keys. The game continues running until the window is closed.

## Features

- Classic Snake game mechanics.
- Control the snake using the arrow keys.
- Continuous game loop with smooth snake movement.

## Setup

To set up and run the Snake game program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py` file and the `snake.py` module in the same directory.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

## How to Use

1. Run the program.
2. Control the snake using the arrow keys:
   - `Up` arrow key to move up.
   - `Down` arrow key to move down.
   - `Left` arrow key to move left.
   - `Right` arrow key to move right.
3. The snake will move continuously until the window is closed.
4. Click on the Turtle graphics window to close it.

## Code Explanation

### Screen Setup

The program initializes the screen with a black background and sets up the title and dimensions.

```python
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
```

### Snake Control

The snake object is created and keyboard listeners are set up to control the snake's direction.

```python
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

### Game Loop

The main game loop keeps the game running, updating the screen and moving the snake at regular intervals.

```python
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
```

## Dependencies

- Python 3.x
- `turtle` module (usually included with Python)

Ensure that `main.py` and `snake.py` are in the same directory where you run the script.

## Conclusion

The Snake game program provides a simple and interactive way to play the classic Snake game using the Turtle graphics module. It demonstrates basic user input handling, continuous game loop, and graphical output. Enjoy playing the Snake game and have fun controlling the snake!
