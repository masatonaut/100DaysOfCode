# Password-Manager

Password-Manager is a simple Python GUI application that helps you generate and store secure passwords for different websites. The application uses the Tkinter library for the graphical user interface.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `pyperclip` module (for copying passwords to clipboard)

You can install `pyperclip` using pip:

```
pip install pyperclip
```

## Files

- `main.py`: The main script that runs the Password-Manager application.
- `logo.png`: An image file used for the application logo.

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Install the `pyperclip` module using pip if you haven't already:
   ```sh
   pip install pyperclip
   ```
3. Download or clone this repository to your local machine.
4. Make sure `main.py` and `logo.png` are in the same directory.
5. Navigate to the directory containing `main.py`.
6. Run the `main.py` script:
   ```sh
   python main.py
   ```
7. A GUI window will appear with fields for website, email/username, and password. You can generate a secure password and save your credentials.

### Features

- **Generate Password**: Click the "Generate Password" button to create a secure, random password. The password will be automatically copied to your clipboard.
- **Save Password**: Enter the website, email/username, and password, then click "Add" to save your credentials to a file named `data.txt`.

## Code Explanation

### Import Libraries

```python
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
```

- Imports Tkinter for GUI and message box functionalities.
- Imports random functions for password generation.
- Imports `pyperclip` for clipboard operations.

### Password Generation

```python
def generate_password():
    letters = [...]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
```

- Generates a random password using letters, numbers, and symbols.
- Shuffles the password components to ensure randomness.
- Displays the generated password in the password entry field and copies it to the clipboard.

### Save Password

```python
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} "
            f"\nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
```

- Retrieves user input from entry fields.
- Validates that the website and password fields are not empty.
- Displays a confirmation dialog with the entered details.
- If confirmed, appends the data to `data.txt` and clears the entry fields.

### UI Setup

```python
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
```

- Creates the main window and configures padding.
- Sets up the canvas with a logo image.
- Adds labels for website, email/username, and password fields.
- Adds entry fields for user input and sets default focus and email.
- Adds buttons for generating passwords and saving data.
- Starts the Tkinter main event loop to display the window and handle user interactions.
