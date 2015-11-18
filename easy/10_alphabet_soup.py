# Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters
# in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.

def AlphabetSoup(a_string):
    list_of_chars = []

    for char in a_string.lower():
        list_of_chars.append(char)

    ordered_list = sorted(list_of_chars)
    alphabetical_string = ''.join(ordered_list)

    return alphabetical_string


