# Using the Python language, have the function WordCount(str) take the str string parameter being passed and return the
# number of words the string contains (ie. "Never eat shredded wheat" would return 4). Words will be separated by
# single spaces.


def WordCount(a_string):
    words = a_string.split()
    return len(words)
