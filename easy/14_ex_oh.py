#  Using the Python language, have the function ExOh(str) take the str parameter being passed and return the string true
# if there is an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered
# in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should return false
# because there are 6 x's and 5 o's.

def ExOh(a_string):
    x_count = 0
    o_count = 0
    for char in a_string:
        if char == "x":
            x_count += 1
        elif char == "o":
            o_count += 1
    if x_count == o_count:
        return "true"
    return "false"
