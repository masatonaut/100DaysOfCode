## Blind Auction: A Python Script for Managing Anonymous Bidding

This Python script facilitates a blind auction process where bidders can anonymously submit their bids without knowing the amounts others have offered. The program maintains a record of bids and determines the highest bidder once the bidding period ends.

### Introduction

The blind auction script is designed to streamline the bidding process by concealing bid amounts until the end, ensuring fair competition among participants. It employs basic Python functionalities to handle user input, record bids, and identify the winning bidder.

### Features

- **Anonymous Bidding**: Bidders submit their bids without visibility into others' offers.
- **Automatic Winner Determination**: Once bidding concludes, the script reveals the highest bidder and their bid.
- **Clear Screen Functionality**: Utilizes the `os` module to clear the screen after each bid, enhancing user experience.

### How to Use

1. **Running the Script**: Execute the Python script `main.py` in your preferred environment. Ensure you have Python installed.
2. **Bidding Process**: Follow the prompts to input your name and bid amount. You'll be asked if there are additional bidders.
3. **End of Bidding**: When no more bidders exist, the script will announce the winner and their bid.

### What You Need to Know

- **main.py**: The main script containing the bidding logic and user interaction.
- **art.py**: The `logo` variable imported from this file displays the program's logo at the start.

#### main.py

- Records bids and bidder names.
- Utilizes a loop to enable continuous bidding until all participants have submitted their offers.
- Calls `find_highest_bidder()` to determine the winning bidder and their bid.

### Setup

To set up the blind auction script on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure `main.py` and `art.py` are accessible in your Python environment.
2. **Run the Script**: Execute `main.py` using a Python interpreter.
3. **Follow the Prompts**: Input your name, bid amount, and whether there are additional bidders as prompted.

### Dependencies

- Python 3.x
- The `art.py` file for displaying an ASCII logo at the start of the program, enhancing the user interface.

Experience the excitement of a blind auction with this Python script, perfect for simulating fair bidding processes in various scenarios!
