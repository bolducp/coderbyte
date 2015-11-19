# Using the Python language, have the function NumberEncoding(str) take the str parameter and encode the message
# according to the following rule: encode every letter into its corresponding numbered position in the alphabet.
# Symbols and spaces will also be used in the input. For example: if str is "af5c a#!" then your program should
# return 1653 1#!.

def NumberEncoding(a_string):
    letter_num_encoder = create_letter_num_dict()
    encoded_string =''
    for char in a_string.lower():
        if char.isalpha():
            encoded_string += str(letter_num_encoder[char])
        else:
            encoded_string += char
    return encoded_string


def create_letter_num_dict():
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = range(1, 27)
    letter_num_dict = {key: value for key, value in zip(letters, nums)}
    return letter_num_dict
