# Snake Game Program

This is a Python implementation of the classic Snake game using the Turtle graphics module. The program allows users to control the snake using the arrow keys, navigate it around the screen, and collect food to grow the snake and increase the score. The game ends if the snake collides with the walls or its own tail.

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

This program is an enhanced implementation of the classic Snake game. The snake moves around the screen, collects food to grow, and the score increases with each food item collected. The game ends if the snake collides with the walls or its own tail.

## Features

- Classic Snake game mechanics with food and score tracking.
- Control the snake using the arrow keys.
- Continuous game loop with smooth snake movement.
- Collision detection with food, walls, and the snake's own tail.
- Score display and game over screen.

## Setup

To set up and run the Snake game program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py` file and the `snake.py`, `food.py`, and `scoreboard.py` modules in the same directory.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

````

## How to Use

1. Run the program.
2. Control the snake using the arrow keys:
   - `Up` arrow key to move up.
   - `Down` arrow key to move down.
   - `Left` arrow key to move left.
   - `Right` arrow key to move right.
3. The snake will move continuously and can collect food to grow and increase the score.
4. The game will end if the snake collides with the walls or its own tail.
5. Click on the Turtle graphics window to close it.

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

The snake object is created along with food and scoreboard objects. Keyboard listeners are set up to control the snake's direction.

```python
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

### Game Loop

The main game loop keeps the game running, updating the screen and moving the snake at regular intervals. It includes collision detection with food, walls, and the snake's own tail.

```python
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
```

## Dependencies

- Python 3.x
- `turtle` module (usually included with Python)

Ensure that `main.py`, `snake.py`, `food.py`, and `scoreboard.py` are in the same directory where you run the script.

## Conclusion

The Snake game program provides an interactive and fun way to play the classic Snake game with enhanced features such as food collection, score tracking, and collision detection. It demonstrates advanced use of the Turtle graphics module, including handling user input, managing game state, and rendering graphics. Enjoy playing the Snake game and have fun controlling the snake!
````
