# Coffee Machine Program

This is a Python implementation of a simple coffee machine simulator. The program allows users to select a type of coffee, checks if the machine has enough resources to make the coffee, processes the payment, and then dispenses the coffee if everything is in order.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Code Explanation](#code-explanation)
  - [Functions](#functions)
- [Dependencies](#dependencies)
- [Conclusion](#conclusion)

## Introduction

This coffee machine program simulates the operations of a real coffee machine. It supports three types of coffee: espresso, latte, and cappuccino. The machine checks for sufficient resources, processes coin payments, and dispenses the selected coffee.

## Features

- Menu options for three types of coffee: espresso, latte, and cappuccino.
- Resource management to ensure enough ingredients are available.
- Coin processing for payments.
- Transaction handling to provide change and update profit.
- Simple user interface for selecting coffee and displaying machine status.

## Setup

To set up and run the coffee machine program on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure the script is saved as `main.py`.
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
   - Type "report" to see the current status of the machine's resources.
   - Type "off" to turn off the machine.
4. Follow the prompts to insert coins if you chose a coffee.
5. The machine will check resources, process the payment, and dispense the coffee if everything is in order.
6. If resources are insufficient or the payment is inadequate, the machine will notify you.

## Code Explanation

### Functions

#### `is_resource_sufficient(order_ingredients)`

Checks if there are enough resources to make the chosen drink. Returns `True` if sufficient, otherwise `False`.

#### `process_coins()`

Prompts the user to insert coins and calculates the total amount inserted. Returns the total value.

#### `is_transaction_successful(money_received, drink_cost)`

Checks if the inserted money is sufficient to cover the drink cost. If so, it updates the profit and returns `True`. Otherwise, it returns `False` and refunds the money.

#### `make_coffee(drink_name, order_ingredients)`

Deducts the required ingredients from the machine's resources and simulates the dispensing of the coffee.

## Dependencies

- Python 3.x

## Conclusion

This coffee machine program is a simple simulation of a real coffee machine, demonstrating basic concepts of resource management, user interaction, and transaction handling in Python. You can extend the functionality by adding more drink options, improving the user interface, or integrating with a real payment system. Enjoy your virtual coffee making!
