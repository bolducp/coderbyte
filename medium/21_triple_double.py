#  Using the Python language, have the function TripleDouble(num1,num2) take both parameters being passed, and return 1
# if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# For example: if num1 equals 451999277 and num2 equals 41177722899, then return 1 because in the first parameter you
# have the straight triple 999 and you have a straight double, 99, of the same number in the second parameter.
#  If this isn't the case, return 0.


def TripleDouble(num1, num2):
    num1_triples = find_triples(num1)
    num2_doubles = find_doubles(num2)

    for num in num1_triples:
        if num in num2_doubles:
            return 1
    return 0


def find_triples(a_num):
    triple_nums = []

    consecutive_count = 1
    current_num = str(a_num)[0]

    for index in xrange(1, len(str(a_num))):
        if str(a_num)[index] == current_num:
            consecutive_count += 1
            if consecutive_count == 3:
                triple_nums.append(current_num)
        else:
            consecutive_count = 1
            current_num = str(a_num)[index]
    return triple_nums


def find_doubles(a_num):
    double_nums = []

    consecutive_count = 1
    current_num = str(a_num)[0]

    for index in xrange(1, len(str(a_num))):
        if str(a_num)[index] == current_num:
            consecutive_count += 1
            if consecutive_count == 2:
                double_nums.append(current_num)
        else:
            consecutive_count = 1
            current_num = str(a_num)[index]
    return double_nums



