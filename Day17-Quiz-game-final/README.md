# Coffee Machine Program

This is a Python implementation of an advanced coffee machine simulator. The program uses separate modules to manage the menu, coffee making process, and money transactions. Users can select a type of coffee, and the program will handle resource checking, payment processing, and coffee dispensing.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
  - [Classes and Methods](#classes-and-methods)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This coffee machine program simulates the operations of a real coffee machine using a modular approach. It supports multiple types of coffee and manages resources and transactions efficiently.

## Features

- Modular design with separate classes for menu, coffee maker, and money transactions.
- Menu options for various types of coffee.
- Resource management to ensure enough ingredients are available.
- Coin processing for payments.
- Simple user interface for selecting coffee and displaying machine status.

## Setup

To set up and run the coffee machine program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure you have the `main.py`, `menu.py`, `coffee_maker.py`, and `money_machine.py` files in the same directory.
2. **Run the Script**: Execute the script using a Python interpreter.
   ```sh
   python3 main.py
   ```

## How to Use

1. Run the program.
2. You will be prompted with the question: "What would you like? (espresso/latte/cappuccino):".
3. Enter your choice:
   - Type "espresso" for an espresso.
   - Type "latte" for a latte.
   - Type "cappuccino" for a cappuccino.
   - Type "report" to see the current status of the machine's resources and money.
   - Type "off" to turn off the machine.
4. Follow the prompts to insert coins if you chose a coffee.
5. The machine will check resources, process the payment, and dispense the coffee if everything is in order.
6. If resources are insufficient or the payment is inadequate, the machine will notify you.

## Code Explanation

### Classes and Methods

The program uses three main classes to manage different aspects of the coffee machine:

1. **Menu**:

   - `get_items()`: Returns a string of available menu items.
   - `find_drink(order_name)`: Searches the menu for a drink by name and returns the drink object if found.

2. **CoffeeMaker**:

   - `report()`: Prints a report of current resources.
   - `is_resource_sufficient(drink)`: Checks if there are enough resources to make the chosen drink.
   - `make_coffee(order)`: Deducts the required ingredients from the resources and simulates the dispensing of the coffee.

3. **MoneyMachine**:
   - `report()`: Prints a report of the current money.
   - `make_payment(cost)`: Processes the coins inserted by the user and checks if the payment is sufficient. Returns `True` if payment is successful, otherwise `False`.

### Main Script (`main.py`)

The main script initializes instances of `MoneyMachine`, `CoffeeMaker`, and `Menu` classes. It then enters a loop where it:

- Prompts the user for input.
- Handles turning off the machine and printing reports.
- Checks if the selected drink can be made and if the payment is successful.
- Makes the coffee if all conditions are met.

```python
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
```

## Dependencies

- Python 3.x

Ensure that `menu.py`, `coffee_maker.py`, and `money_machine.py` are in the same directory as `main.py`.

## Conclusion

This advanced coffee machine program provides a modular and efficient way to simulate a real coffee machine's operations. It demonstrates the use of classes and methods to manage different functionalities and offers a user-friendly interface for interacting with the machine. Enjoy exploring and extending this coffee machine simulator!
