import sys
from stats import word_counter, letter_counter, character_list

def myFunc(e):
    return e['num']

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

        
    book_content = get_book_text(sys.argv[1])
    num_words = word_counter(book_content)
    num_letters = letter_counter(book_content)
    char_list = character_list(num_letters)
    char_list.sort(reverse=True,key=myFunc)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")
    

main()