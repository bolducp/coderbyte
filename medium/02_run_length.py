# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string
# using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character
# and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would
# return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.


def RunLength(a_str):
    compressed_string = ''
    start_indices = get_new_letter_start_indices(a_str)
    string_end_index = len(a_str)
    start_indices.append(string_end_index)

    for index in range(len(start_indices) - 1):
        num_occurrences = start_indices[index + 1] - start_indices[index]
        letter = a_str[start_indices[index]]
        compressed_string += (str(num_occurrences) + letter)

    return compressed_string


def get_new_letter_start_indices(a_str):
    letter_start_indices = [0]
    for index in xrange(1, len(a_str)):
        if a_str[index] != a_str[index - 1]:
            letter_start_indices.append(index)
    return letter_start_indices



# keep this function call here
# to see how to enter arguments in Python scroll down
print RunLength(raw_input())



















