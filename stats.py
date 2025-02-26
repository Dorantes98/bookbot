def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
frankenstein = get_book_text("books/frankenstein.txt")

def count_words(text):
    return len(text.split())

word_count = count_words(frankenstein)

def count_characters(text):
    char_counts = {}

    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

num_of_chars = count_characters(frankenstein)
