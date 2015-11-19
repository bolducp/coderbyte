#  Using the Python language, have the function VowelCount(str) take the str string parameter being passed and return
# the number of vowels the string contains (ie. "All cows eat grass" would return 5). Do not count y as a vowel for
# this challenge.

def VowelCount(a_string):
    vowels = 'aeiou'
    vowel_count = 0
    for char in a_string.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count

