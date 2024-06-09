# NATO Phonetic Alphabet Converter

This Python program converts a user-input word into its NATO phonetic alphabet equivalent. It reads the NATO phonetic alphabet from a CSV file and uses it to create a dictionary for conversion.

## Requirements

- Python 3.x
- `pandas` module

You can install the `pandas` module using pip:

```
pip install pandas
```

## Files

- `main.py`: The main script that runs the conversion.
- `nato_phonetic_alphabet.csv`: A CSV file containing the NATO phonetic alphabet.

## How to Use

1. Ensure you have `nato_phonetic_alphabet.csv` in the same directory as `main.py`.
2. Run the `main.py` script.
3. Enter a word when prompted.
4. The program will output the word's NATO phonetic alphabet equivalent.

## Code Explanation

### Import Libraries

```python
import pandas
```

Imports the necessary `pandas` library.

### Load Data

```python
data = pandas.read_csv("nato_phonetic_alphabet.csv")
```

Reads the NATO phonetic alphabet data from the CSV file.

### Create Phonetic Dictionary

```python
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
```

Creates a dictionary where each letter is mapped to its corresponding phonetic code word.

### Convert User Input

```python
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
```

- Prompts the user to enter a word.
- Converts the word to uppercase.
- Converts each letter of the word to its phonetic code word using the dictionary.
- Outputs the list of phonetic code words.

## Example

If the user inputs "HELLO", the output will be:

```
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```
