# Hirst Painting Dot Art Program

This is a Python implementation of a dot painting inspired by the artist Damien Hirst. The program uses the Turtle graphics module to create a grid of colored dots on the screen.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This program generates a piece of dot art inspired by Damien Hirst. It uses a list of predefined colors to randomly color each dot, creating a visually appealing grid pattern. The Turtle graphics module is used to handle the drawing operations.

## Features

- Creates a 10x10 grid of colored dots.
- Uses a predefined color palette.
- Randomly selects colors for each dot from the palette.
- Fast drawing speed for quick rendering.

## Setup

To set up and run the dot painting program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py` file.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

## How to Use

1. Run the program.
2. The Turtle graphics window will open and start drawing the dot painting.
3. The window will display the completed dot painting.
4. Click on the window to close it.

## Code Explanation

### Color Palette

A list of RGB tuples is predefined to represent the colors used in the dot painting.

```python
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]
```

### Turtle Setup

The Turtle module is configured to use RGB colors and a fast drawing speed. The turtle is initially positioned off-screen to start drawing.

```python
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
```

### Drawing the Grid

The turtle moves to the starting position and begins drawing dots in a grid pattern. It moves forward to draw each dot and adjusts its position at the end of each row.

```python
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
```

### Exiting the Program

The program waits for a click on the Turtle graphics window to close.

```python
screen = turtle_module.Screen()
screen.exitonclick()
```

## Dependencies

- Python 3.x
- `turtle` module (usually included with Python)

Ensure that `main.py` is in the same directory where you run the script.

## Conclusion

This dot painting program provides a fun and interactive way to create art using the Turtle graphics module. It demonstrates basic Turtle graphics operations and random color selection from a predefined palette. Feel free to experiment with different color palettes and grid sizes to create your own unique dot paintings. Enjoy creating your dot art!
