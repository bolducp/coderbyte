#  Using the Python language, have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher
# shift on it using the num parameter as the shifting number. A Caesar Cipher works by shifting each letter in the
# string N places down in the alphabet (in this case N will be num). Punctuation, spaces, and capitalization should
# remain intact. For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

def CaesarCipher(a_str, num):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_string = ''

    for char in a_str:
        if char not in lower_letters and char not in upper_letters:
            encoded_string += char
        elif char.isupper():
            index = upper_letters.index(char)
            new_index = (index + num) % 25
            if (index + num) > 25:
                new_index = new_index - 1
            encoded_string += upper_letters[new_index]
        else:
            index = lower_letters.index(char)
            new_index = (index + num) % 25
            if (index + num) > 25:
                new_index = new_index - 1
            encoded_string += lower_letters[new_index]
    return encoded_string


