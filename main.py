def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
frankenstein = get_book_text("books/frankenstein.txt")

def count_words(text):
    return len(text.split())

word_count = count_words(frankenstein)

def main():
    # print(frankenstein)
    print(f"{word_count} words found in the document")

if __name__ == '__main__':
    main()