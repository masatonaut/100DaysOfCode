# Mile-To-Km-Converter

Mile-To-Km-Converter is a simple Python GUI application that converts miles to kilometers using the Tkinter library.

## Requirements

- Python 3.x

## Files

- `main.py`: The main script that runs the Mile-To-Km-Converter application.

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the directory containing `main.py`.
4. Run the `main.py` script:
   ```
   python main.py
   ```
5. A GUI window will appear with an input box, two buttons, and a label.
6. Enter a distance in miles into the input box.
7. Click the "Convert" button to convert the entered miles to kilometers. The converted value will be displayed in the label.
8. You can click the "Reset" button to clear the input and output fields.

## Code Explanation

### Import Libraries

```python
from tkinter import *
```

Imports the Tkinter library for creating the GUI.

### Convert Miles to Kilometers Function

```python
def convert_miles_to_km():
    try:
        miles = float(input_entry.get())
        km = miles * 1.60934
        result_label.config(text=f"{km:.2f} Km")
    except ValueError:
        result_label.config(text="Please enter a valid number")
```

- `convert_miles_to_km` function is called when the "Convert" button is clicked.
- Retrieves the value from the input entry box, converts it to a float, and calculates the kilometers.
- Updates the result label with the converted value.
- If the input is not a valid number, an error message is displayed.

### Reset Function

```python
def reset():
    input_entry.delete(0, END)
    result_label.config(text="0 Km")
```

- `reset` function clears the input entry box and resets the result label.

### Main Window Setup

```python
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
```

- Creates the main window using `Tk()`.
- Sets the window title to "Mile to Km Converter".
- Sets the minimum size of the window.
- Adds padding around the window.

### Label Setup

```python
input_label = Label(text="Miles", font=("Arial", 14))
input_label.grid(column=0, row=0)

result_label = Label(text="0 Km", font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)
```

- Creates a label for miles input with specified font.
- Places the label in the grid at column 0, row 0.
- Creates a label for displaying the result with specified font and initial text "0 Km".
- Places the label in the grid at column 1, row 1.

### Entry Setup

```python
input_entry = Entry(width=10)
input_entry.grid(column=1, row=0)
```

- Creates a text entry box with a width of 10.
- Places the entry box in the grid at column 1, row 0.

### Button Setup

```python
convert_button = Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=1, row=2)
```

- Creates a button with text "Convert" and associates it with `convert_miles_to_km` function.
- Places the button in the grid at column 0, row 2.
- Creates a button with text "Reset" and associates it with `reset` function.
- Places the button in the grid at column 1, row 2.

### Main Loop

```python
window.mainloop()
```

- Starts the Tkinter main event loop, which waits for user interactions and updates the GUI accordingly.

## Example

When you run the program and enter a value in miles, clicking the "Convert" button will display the converted kilometers in the label. Clicking the "Reset" button will clear the input and reset the output.
