## BookBot

BookBot is a simple Python-based text analysis tool that reads a book file, counts the number of words, and analyzes the frequency of individual alphabetical characters.

### Features
- Reads text from a book file
- Counts the total number of words in the book
- Counts the occurrences of each character (case-insensitive)
- Sorts and displays character counts for alphabetical characters in descending order

### Installation
#### Prerequisites
Ensure you have Python 3 installed on your system. You can check your Python version using:
```sh
python3 --version
```

#### Clone the Repository
```sh
git clone https://github.com/yourusername/bookbot.git
cd bookbot
```

### Usage
Run the script with a text file as an argument:
```sh
python3 main.py <path_to_book>
```
For example:
```sh
python3 main.py books/sample.txt
```

#### Example Output
```
============ BOOKBOT ============
Analyzing book found at books/sample.txt...
----------- Word Count ----------
12345
--------- Character Count -------
e: 10234
t: 8765
a: 7890
...
```

### File Overview
#### `main.py`
This is the entry point of the program. It:
- Accepts a file path as a command-line argument.
- Calls functions from `stats.py` to process the text.
- Prints the word count and sorted character counts.

#### `stats.py`
Contains helper functions:
- `get_book_text(filepath)`: Reads the book text from a file.
- `count_words(text)`: Counts and returns the total number of words in the text.
- `count_characters(text)`: Counts occurrences of each character (case-insensitive).
- `sort_char_counts(char_counts)`: Sorts alphabetical character counts in descending order.

### Notes
- The character count only includes alphabetical characters (ignoring numbers, punctuation, etc.).
- The program handles case-insensitivity by converting all text to lowercase.

### License
This project is licensed under the MIT License.

---
Happy coding with BookBot! 🚀