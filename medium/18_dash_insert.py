# Using the Python language, have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and
# insert asterisks ('*') between each two even numbers in str. For example: if str is 4546793 the output should be
# 454*67-9-3. Don't count zero as an odd or even number.

def DashInsertII(num_str):
    encoded_string = ''
    for index in xrange(len(num_str) - 1):
        encoded_string += num_str[index]
        if is_odd(int(num_str[index])) and is_odd(int(num_str[index + 1])):
            encoded_string += '-'
        elif is_even(int(num_str[index])) and is_even(int(num_str[index + 1])):
            encoded_string += '*'
    encoded_string += num_str[-1]
    return encoded_string


def is_even(num):
    if num == 0:
        return False
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0