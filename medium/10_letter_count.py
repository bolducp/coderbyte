# Have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest
# number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has
# 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating letters
# return -1. Words will be separated by spaces.

def repeated_letter_hist(word):
    histogram = {}
    for letter in word:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            continue
        else:
            histogram[letter] = histogram.get(letter, 0) + 1
    maximum = max(histogram.values())
    return maximum


def LetterCount(a_str):
    split_string = a_str.split()
    max_count_repeats = 1
    word_with_most = ''

    for word in split_string:
        if repeated_letter_hist(word) > max_count_repeats:
            max_count_repeats = repeated_letter_hist(word)
            word_with_most = word

    if max_count_repeats > 1:
        return word_with_most
    return -1



# keep this function call here
# to see how to enter arguments in Python scroll down
print LetterCount(raw_input())