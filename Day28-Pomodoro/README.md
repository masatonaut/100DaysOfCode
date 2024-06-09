# Pomodoro Timer

Pomodoro Timer is a simple Python GUI application that helps you manage your work and break intervals using the Pomodoro Technique. The application uses the Tkinter library for the graphical user interface.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Files

- `main.py`: The main script that runs the Pomodoro Timer application.
- `tomato.png`: An image file used for the timer display.

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Download or clone this repository to your local machine.
3. Make sure `main.py` and `tomato.png` are in the same directory.
4. Navigate to the directory containing `main.py`.
5. Run the `main.py` script:
   ```sh
   python main.py
   ```
6. A GUI window will appear with a start button, reset button, and a timer display.

### Timer Functionality

- **Start Button**: Starts the timer for a work session or break session based on the current state.
- **Reset Button**: Resets the timer and clears the progress.

### Pomodoro Technique

- **Work Session**: 1 minute (customizable)
- **Short Break**: 5 minutes (customizable)
- **Long Break**: 20 minutes (customizable)
- After 4 work sessions, a long break is triggered.

## Code Explanation

### Import Libraries and Set Constants

```python
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
```

- Imports Tkinter for GUI and math for calculations.
- Defines color constants and timing settings for work, short break, and long break intervals.
- Initializes session counter (`reps`) and timer ID (`timer`).

### Timer Reset Function

```python
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
```

- Cancels the current timer.
- Resets the timer display, title, check marks, and session counter.

### Timer Start Function

```python
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
```

- Increments the session counter.
- Determines whether to start a work session, short break, or long break based on the session count.
- Updates the title label accordingly.

### Countdown Mechanism

```python
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
```

- Calculates minutes and seconds from the countdown value.
- Formats seconds to always show two digits.
- Updates the timer text on the canvas.
- If the countdown is not finished, continues counting down every second.
- If the countdown is finished, starts the next timer session and updates the check marks.

### UI Setup

```python
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
```

- Creates the main window and configures its properties.
- Sets up the title label, canvas with timer text, start and reset buttons, and check marks label.
- Positions the elements using a grid layout.
- Starts the Tkinter main event loop to display the window and handle user interactions.
