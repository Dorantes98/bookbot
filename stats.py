# Function to read the entire text from a file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Function to count the number of words in a given text
def count_words(text):
    # .split() divides the text into words using whitespace
    return len(text.split())

# Function to count every character in the text (after converting to lowercase)
def count_characters(text):
    char_counts = {}
    # Convert the text to lowercase so 'A' and 'a' are counted as the same character
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Function to sort alphabetical characters by count (greatest to least)
def sort_char_counts(char_counts):
    # Create a list of single-pair dictionaries for alphabetical characters only
    alpha_counts = [{char: count} for char, count in char_counts.items() if char.isalpha()]
    # Sort the list in descending order by the count value
    alpha_counts.sort(key=lambda d: list(d.values())[0], reverse=True)
    return alpha_counts
