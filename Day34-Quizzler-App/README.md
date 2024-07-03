## Quizzler

Quizzler is a quiz application built using Python and the `tkinter` library for the graphical user interface (GUI). The app fetches quiz questions from the Open Trivia Database (OpenTDB) API and presents them to the user. Users answer True/False questions and receive feedback on their answers.

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages**:
   ```bash
   pip install requests
   ```

### Files and Directories

- **main.py**: Entry point of the application. It initializes the quiz.
- **data.py**: Handles fetching quiz data from the OpenTDB API.
- **question_model.py**: Defines the Question class.
- **quiz_brain.py**: Contains the logic for handling quiz questions and scoring.
- **ui.py**: Manages the graphical user interface using `tkinter`.
- **images**: Contains the True/False button images.

### Usage

1. **Run the application**:

   ```bash
   python main.py
   ```

2. **Answering Questions**:
   - The application will display a series of True/False questions.
   - Click the "True" or "False" button to submit your answer.
   - The background will turn green for correct answers and red for incorrect answers.
   - The score will be updated and displayed at the top.

### Code Overview

#### data.py

```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
```

- Fetches 10 True/False questions from the OpenTDB API.

#### question_model.py

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

- Defines the Question class with text and answer attributes.

#### quiz_brain.py

```python
import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
```

- Manages the quiz logic, keeps track of the score, and checks answers.

#### ui.py

```python
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
```

- Constructs the GUI, displays questions, and updates the interface based on user interaction.

### Notes

- Ensure that the `images` directory contains `true.png` and `false.png` images for the buttons.
- Adjust the parameters in `data.py` to fetch different types or amounts of questions if desired.

This application demonstrates how to combine web APIs with a GUI to create an interactive quiz experience in Python.
