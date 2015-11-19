# Using the Python language, have the function LookSaySequence(num) take the num parameter being passed and return the
# next number in the sequence according to the following rule: to generate the next number in a sequence read off the
# digits of the given number, counting the number of digits in groups of the same digit. For example, the sequence
# beginning with 1 would be: 1, 11, 21, 1211, ... The 11 comes from there being "one 1" before it and the 21 comes
# from there being "two 1's" before it. So your program should return the next number in the sequence given num.

def LookSaySequence(num):
    digits_list = []

    starting_char = str(num)[0]
    char_count = 1
    str_num = str(num) + "x"

    for char in str_num[1:]:
        if char == starting_char:
            char_count += 1
        else:
            digits_list.append(str(char_count))
            digits_list.append(starting_char)
            starting_char = char
            char_count = 1

    joined_string = int("".join(digits_list))
    return joined_string


