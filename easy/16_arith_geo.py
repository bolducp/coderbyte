# Using the Python language, have the function ArithGeo(arr) take the array of numbers stored in arr and return the
# string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric
# pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference
# between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied
# by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

def ArithGeo(arr):
    if is_arithmetic(arr):
        return "Arithmetic"
    elif is_geometric(arr):
        return "Geometric"
    else:
        return -1


def is_arithmetic(arr):
    first_diff = arr[1] - arr[0]
    for num in xrange(len(arr)- 1):
        if arr[num + 1] - arr[num] != first_diff:
            return False
    return True


def is_geometric(arr):
    first_multiplier = arr[1] // arr[0]
    for num in xrange(len(arr)- 1):
        if arr[num + 1] // arr[num] != first_multiplier:
            return False
    return True

