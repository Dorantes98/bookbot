from stats import count_words, word_count, frankenstein, count_characters
from stats import num_of_chars, get_book_text, sort_char_counts

def main():
    # print(frankenstein)
    # print(f"{word_count} words found in the document")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # Get the sorted list of alphabetical character counts
    sorted_counts = sort_char_counts(num_of_chars)
    # Print each character and count in the desired format
    for char_count in sorted_counts:
        for char, count in char_count.items():
            print(f"{char}: {count}")

if __name__ == '__main__':
    main()