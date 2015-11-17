# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence
#  by either returning the string true or false. The str parameter will be composed of + and = symbols with several
# letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one letter.


def SimpleSymbols(str):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for num in xrange(len(str)):
        if str[0] in letters or str[-1] in letters:
            return False
        elif str[num] in letters:
            if str[num - 1] != "+" or str[num + 1] != "+":
                return False
    return True



# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleSymbols(raw_input())