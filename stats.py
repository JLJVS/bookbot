def word_count(text: str) -> int:
    '''
    Counts the number of words in the given text (string) and returns the word count as an integer
    '''
    words = text.split()
    return len(words)

def char_count(text: str) -> dict:
    text_lowered = text.lower()
    characters = {}
    for character in text_lowered:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_char_count(char_dict: dict[str, int]):
    '''
    Sorts the results in char count in alphabetical order and returns them as a list of dictonaries
    '''

    valid_keys = [key for key in char_dict.keys() if key.isalpha() ]
    
    sorted_char_count = []

    for key in valid_keys:
        sorted_char_count.append({"character": key, "count": char_dict[key]})
    sorted_char_count.sort(key= lambda x: x["count"], reverse =True)
    return sorted_char_count