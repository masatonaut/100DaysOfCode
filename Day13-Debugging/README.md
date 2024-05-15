# Debugging Python Script

This Python script demonstrates common debugging techniques to identify and fix bugs in a series of code snippets. Each section includes an example of a problem, steps to reproduce the bug, and instructions for fixing it.

### Introduction

Debugging is an essential skill for any programmer. This script provides a hands-on approach to understanding common issues and debugging techniques in Python. It covers various scenarios, from logical errors to improper use of functions and incorrect user inputs.

### Features

- **Problem Descriptions**: Each section starts with a brief description of the problem.
- **Bug Reproduction**: Steps to reproduce the bug are included to understand the issue better.
- **Error Fixing**: Instructions on how to fix the errors are provided.
- **Debugging Techniques**: Emphasizes the use of print statements and debuggers to identify issues.

### How to Use

1. **Read the Problem Description**: Understand the context and the issue in the code snippet.
2. **Reproduce the Bug**: Run the provided code to see the error.
3. **Follow the Fix Instructions**: Apply the suggested fixes and verify the solution by running the code again.
4. **Use Debugging Tools**: Utilize print statements and debuggers as shown to aid in the debugging process.

### Code Snippets and Fixes

#### 1. Describe Problem

**Problem**: The function doesn't print the message "You got it" as expected.

```python
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
```

**Fix**: The range should include 20. Modify the loop to iterate correctly.

```python
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()
```

#### 2. Reproduce the Bug

**Problem**: Randomly select a dice image but may encounter an index error.

```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```

**Fix**: Ensure the random number is within the correct range. Use `randint(1, 6)`.

```python
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```

#### 3. Play Computer

**Problem**: Incorrect logic for determining generational labels.

```python
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
```

**Fix**: Adjust the conditions to include the boundaries correctly.

```python
year = int(input("What's your year of birth?"))
if 1981 <= year <= 1996:
  print("You are a millenial.")
elif year >= 1997:
  print("You are a Gen Z.")
```

#### 4. Fix the Errors

**Problem**: Incorrect indentation and input handling.

```python
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
```

**Fix**: Ensure proper indentation and logic.

```python
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
```

#### 5. Print is Your Friend

**Problem**: The calculation of total words is incorrect due to missing input assignment.

```python
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
```

**Fix**: Add print statements to verify the inputs and calculations.

```python
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
```

#### 6. Use a Debugger

**Problem**: The function mutates a list incorrectly due to a logical error.

```python
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

**Fix**: Verify the logic inside the loop and print the intermediate steps.

```python
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

### Setup

To set up and run the debugging script on your local machine, follow these steps:

1. **Clone the Repository or Download Files**: Ensure the script and any associated files are in the same directory.
2. **Run the Script**: Execute the script using a Python interpreter.
3. **Follow the Instructions**: Apply the debugging steps as described.

### Dependencies

- Python 3.x

### Conclusion

This script provides a comprehensive guide to debugging common issues in Python. By following the provided examples and fixes, you can improve your debugging skills and better understand how to identify and resolve errors in your code.
