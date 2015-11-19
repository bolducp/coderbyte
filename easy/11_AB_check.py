#  Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string
# true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie.
# "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise
# return the string false.

def ABCheck(a_string):

    for index in xrange(len(a_string) - 4):
        if a_string[index] == 'a':
            if a_string[index + 4] == 'b':
                return True
        elif a_string[index] == 'b':
            if a_string[index + 4] == 'a':
                return True
    return False



