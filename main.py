from stats import get_num_words
from stats import get_num_characters
from stats import sorted_dictionary
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
    
def main():
    """
    Main function to execute the script.
    """
    # Path to the book file
    # book_path = 'books/frankenstein.txt'
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        exit(1)
    
    
    # Get the text from the book file
    book_text = get_book_text(book_path)
                              
    num_words = get_num_words(book_text)
    # print(f"{num_words} words found in the document")

    num_of_different_characters = get_num_characters(book_text)
    # print(f"Count : {num_of_different_characters}")
    
    list_of_dicts = sorted_dictionary(num_of_different_characters)
    
    welcome_text = """============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt..."""
    work_count_text = "----------- Word Count ----------"
    char_text = "--------- Character Count -------"
    end_text = "============= END ==============="
    
    print(welcome_text)
    print(work_count_text)
    # Print the number of words found in the document
    print(f"Found {num_words} total words")
    print(char_text)
    for d in list_of_dicts:
        # Print the character and its count    
        print(f"{d["char"]}: {d["count"]}")
    print(end_text)
    
main()