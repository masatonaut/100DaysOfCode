## Flashy: A Python Script for Learning French with Flashcards

This Python script creates a flashcard application for learning French vocabulary. The program uses Tkinter for the graphical user interface (GUI) and Pandas for managing vocabulary data. The flashcards display a French word, which flips to show the English translation after a set time, allowing users to test and improve their language skills interactively.

### Introduction

The Flashy script is designed to assist in learning French by displaying flashcards with vocabulary words. Users can interact with the flashcards, marking words as known or unknown, and the program adjusts the learning material accordingly. This interactive approach helps reinforce memory and retention of new vocabulary.

### Features

- **Interactive Flashcards**: Display French words that flip to show the English translation after a brief period.
- **Progress Tracking**: Keeps track of known and unknown words, updating the learning material based on user input.
- **Easy to Use GUI**: Utilizes Tkinter to create an intuitive and visually appealing interface.

### How to Use

1. **Running the Script**: Execute the Python script in your preferred environment. Ensure you have Python and the required libraries installed.
2. **Using Flashcards**: Follow the on-screen prompts. French words will be displayed on the flashcards, and after a few seconds, they will flip to show the English translation.
3. **Marking Words**: Use the provided buttons to mark whether you know the word (`right` button) or don't know the word (`wrong` button).

### What You Need to Know

- **words_to_learn.csv**: A CSV file that tracks the words you are learning. If it does not exist, the script uses `french_words.csv` as the initial dataset.
- **french_words.csv**: A CSV file containing the initial set of French words and their English translations.
- **images**: A directory containing images for the flashcards and buttons.

#### Code Explanation

- **Data Handling**: The script reads vocabulary data from CSV files using Pandas. It keeps track of words to learn and updates the progress as you interact with the flashcards.
- **GUI Setup**: Tkinter is used to create the main window, canvas for displaying cards, and buttons for user interaction.
- **Card Flipping**: A timer flips the flashcards to reveal the English translation after a set period.

### Setup

To set up the Flashy script on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure the Python script and necessary CSV files (`french_words.csv`, `words_to_learn.csv`) and image files are accessible in your Python environment.
2. **Install Dependencies**: Install the required libraries using pip:
   ```sh
   pip install pandas
   ```
3. **Run the Script**: Execute the script using a Python interpreter:
   ```sh
   python main.py
   ```
4. **Follow the Prompts**: Use the GUI to interact with the flashcards, marking words as known or unknown.

### Dependencies

- Python 3.x
- Pandas
- Tkinter (included with Python standard library)
- Image files for flashcards and buttons (`card_front.png`, `card_back.png`, `wrong.png`, `right.png`)

### Detailed Code Explanation

#### Data Loading and Initialization

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

- Tries to load the progress from `words_to_learn.csv`. If it doesn't exist, loads initial vocabulary from `french_words.csv`.

#### Displaying the Next Card

```python
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
```

- Cancels any existing timer, selects a random word, and sets up the card for display.

#### Flipping the Card

```python
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
```

- Changes the card to show the English translation.

#### Marking a Word as Known

```python
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
```

- Removes the known word from the list and updates the CSV file.

#### GUI Setup

```python
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
```

- Creates the main window, sets up the canvas and buttons, and starts the event loop.
