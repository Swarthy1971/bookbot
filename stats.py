def get_num_words(book_text):
    """
    Counts the number of words in the book text.
    
    Args:
        book_text (str): The content of the book file.
        
    Returns:
        int: The number of words in the book text.
    """
    # Split the text into words and count them
    num_words = 0
    for word in book_text.split():
        num_words += 1
    
    return num_words


def get_num_characters(book_text):
    """
    Counts the number of characters in the book text.
    
    Args:
        book_text (str): The content of the book file.
        
    Returns:
        dict: The number of different characters in the book text.
    """
    # Count the number different characters in the text

    char_data = {}
    for char in book_text.lower():
        if char in char_data:
            char_data[char] += 1
        else:
            char_data[char] = 1

    return char_data


def sorted_dictionary(dictionary):
    """
    Sorts a dictionary by its keys.
    
    Args:
        dictionary (dict): The dictionary to sort.
        
    # Returns:
    #     dict: The sorted dictionary.
    """
    list_of_dictionaries = []
    
    for key, value in dictionary.items():
        if key.isalpha():
            list_of_dictionaries.append({"char": key, "count": value})
            
    def sort_on(dict):
        return dict["count"]
    
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_of_dictionaries
    