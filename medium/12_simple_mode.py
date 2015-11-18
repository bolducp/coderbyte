#  Using the Python language, have the function SimpleMode(arr) take the array of numbers stored in arr and return the
# number that appears most frequently (the mode). For example: if arr contains [10, 4, 5, 2, 4] the output should be 4.
# If there is more than one mode return the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should return 5
# because it appeared first). If there is no mode return -1. The array will not be empty.

def make_histogram(an_array):
    histogram = {}
    for num in an_array:
        histogram[num] = histogram.get(num, 0) + 1
    return histogram

def SimpleMode(an_array):
    histogram = make_histogram(an_array)

    maximum = max(histogram.values())
    if maximum == 1:
        return -1
    maxes = []

    for key in histogram.keys():
        if histogram[key] == maximum:
            maxes.append(key)

    for num in an_array:
        if num in maxes:
            return num


