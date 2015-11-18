# Using the Python language, have the function ArrayAddition(arr) take the array of numbers stored in arr and return
# the string true if any combination of numbers in the array can be added up to equal the largest number in the array,
# otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true
# because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain
# negative numbers.


def ArrayAddition(arr):
    max_num = max(arr)
    possible_totals = []
    arr.remove(max_num)

    for num in arr:
        possible_totals.append(num)
        num_total = num
        arr.remove(num)

        for other_num in arr:
            possible_totals.append(num + other_num)
            num_total += other_num
            possible_totals.append(num_total)

    return max_num in possible_totals




