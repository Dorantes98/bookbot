import sys
from stats import get_book_text, count_words, count_characters, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)

    word_count = count_words(book_text)
    print("----------- Word Count ----------")
    print(word_count)

    # Get character counts and sort them
    char_counts = count_characters(book_text)
    sorted_counts = sort_char_counts(char_counts)
    print("--------- Character Count -------")
    # Print each character and count in the desired format
    for char_count in sorted_counts:
        for char, count in char_count.items():
            print(f"{char}: {count}")

if __name__ == '__main__':
    main()