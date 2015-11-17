def LetterChanges(a_string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encoded_string = ''
    for letter in a_string.lower():
        if letter not in letters:
            encoded_string += letter
        elif letter == 'z':
            encoded_string += 'a'
        else:
          index = letters.index(letter)
          encoded_string += letters[index + 1]
    capitalized_encoded = ''

    for char in encoded_string:
        if char in 'aeiou':
            capitalized_encoded += char.upper()
        else:
            capitalized_encoded += char
    return capitalized_encoded


# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())