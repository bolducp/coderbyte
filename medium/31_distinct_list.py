#  Using the Python language, have the function DistinctList(arr) take the array of numbers stored in arr and determine
# the total number of duplicate entries. For example if the input is [1, 2, 2, 2, 3] then your program should output 2
# because there are two duplicates of one of the elements.

def DistinctList(an_array):
    distinct_array = list(set(an_array))
    num_duplicates = len(an_array) - len(distinct_array)
    return num_duplicates


