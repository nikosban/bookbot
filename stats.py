
def word_counter(content_string):
    word_counter = 0

    word_list = content_string.split()
    for word in word_list:
        word_counter += 1

    return word_counter

def letter_counter(content_string):
    norm_string = content_string.lower()
    letter_list = {}

    for character in norm_string:
        if not character in letter_list:
            letter_list[character] = 0
        letter_list[character] += 1

    return letter_list


def character_list(char_dict):
    formated_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            formated_list.append({"char": key, "num": value})
    
    return formated_list