# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
# Use the Parameter Testing feature in the box below to test your code with different arguments.

def FirstReverse(a_string):
    reversed_string = ''
    for char in a_string[::-1]:
        reversed_string += char
    return reversed_string


# keep this function call here
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())
