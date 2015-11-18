#  Using the Python language, have the function StringScramble(str1,str2) take both parameters being passed and return
# the string true if a portion of str1 characters can be rearranged to match str2, otherwise return the string false.
# For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will
# not be entered with the parameters.

def StringScramble(str1, str2):
    outer_string = str1
    inner_string = str2
    for char in inner_string:
        if char not in outer_string:
            return False
        updated_outer = outer_string.replace(char, "", 1)
        outer_string = updated_outer
    return True
