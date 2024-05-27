# Pong Game Program

This is a Python implementation of the classic Pong game using the Turtle graphics module. The program allows users to control two paddles using the keyboard and play against each other. The game includes collision detection, score tracking, and ball movement.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
  - [Screen Setup](#screen-setup)
  - [Paddle and Ball Control](#paddle-and-ball-control)
  - [Game Loop](#game-loop)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This program is a simple implementation of the classic Pong game. Two players control paddles on either side of the screen, and the objective is to hit the ball back and forth without missing. The game keeps track of the score for both players.

## Features

- Classic Pong game mechanics.
- Two-player paddle control using the keyboard.
- Ball movement with collision detection.
- Score tracking for both players.

## Setup

To set up and run the Pong game program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py` file and the `paddle.py`, `ball.py`, and `scoreboard.py` modules in the same directory.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

````

## How to Use

1. Run the program.
2. Control the paddles using the keyboard:
   - Player 1 (right paddle) uses the `Up` and `Down` arrow keys.
   - Player 2 (left paddle) uses the `w` and `s` keys.
3. The ball will move automatically. The objective is to prevent the ball from going past your paddle.
4. The score will be updated each time a player misses the ball.
5. Click on the Turtle graphics window to close it.

## Code Explanation

### Screen Setup

The program initializes the screen with a black background and sets up the title and dimensions.

```python
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
```

### Paddle and Ball Control

The paddles and ball objects are created, and keyboard listeners are set up to control the paddles' movements.

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

### Game Loop

The main game loop keeps the game running, updating the screen and moving the ball at regular intervals. It includes collision detection with the walls, paddles, and scoring.

```python
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
```

## Dependencies

- Python 3.x
- `turtle` module (usually included with Python)

Ensure that `main.py`, `paddle.py`, `ball.py`, and `scoreboard.py` are in the same directory where you run the script.

## Conclusion

The Pong game program provides an interactive and fun way to play the classic Pong game with two players. It demonstrates advanced use of the Turtle graphics module, including handling user input, managing game state, and rendering graphics. Enjoy playing Pong and have fun competing against a friend!
````
