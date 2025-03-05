import sys
from stats import word_count, char_count, sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    # check if a path is provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # get the path
    path = sys.argv[1]
    
    # do the analysis
    book_text = get_book_text(path)
    words = word_count(book_text)
    char_dict = char_count(book_text)
    sorted_char_dict = sort_char_count(char_dict)

    # print the results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_dict:
        letter, count = entry["character"], entry["count"]
        print(f"{letter}: {count}")
    print("============= END ===============")

main()