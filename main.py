def main():
    book_path = "books/frankenstein.txt"
    text = print_book(book_path)

    # Count words
    count_words(text)

    # Count characters
    count_chars(text)

    # Print a report
    generate_report(count_chars(text), count_words(text), book_path)

def count_words(book):
    word_count = book.split()
    return len(word_count)

def print_book(book_path):
    with open(book_path) as f:
        return f.read()
    
def convert_dict(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"key": char, "num": count})
    return char_list

def sort_on(dict):
    return dict["num"]

def count_chars(book):
    low_book = book.lower()
    char_count = {} 
    for char in low_book:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    char_list = convert_dict(char_count)
    char_list.sort(key=sort_on, reverse=True)  # Note: True for descending order
    return char_list

def generate_report(char_count, word_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    
    for char in char_count:
        print(f"The {char["key"]} character was found {char["num"]} times")
    
    print("--- End report ---")

main()

