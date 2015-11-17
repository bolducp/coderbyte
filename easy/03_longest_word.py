# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.


def LongestWord(sentence):
    longest_word = ''
    for char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
        no_punct_sentence = sentence.replace(char, " ")
    split_sentence = no_punct_sentence.split()

    for word in split_sentence:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word



# keep this function call here
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())
