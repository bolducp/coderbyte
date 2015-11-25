#  Using the Python language, have the function SecondGreatLow(arr) take the array of numbers stored in arr and return
# the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains
# [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers.
# It can get tricky if there's just two numbers!

def SecondGreatLow(arr):
    multiples_removed_list = list(set(arr))
    sorted_list = sorted(multiples_removed_list)

    second_greatest = sorted_list[-2]
    second_lowest = sorted_list[1]

    return "%d %d" % (second_lowest, second_greatest)