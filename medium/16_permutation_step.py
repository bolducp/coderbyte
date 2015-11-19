#  Using the Python language, have the function PermutationStep(num) take the num parameter being passed and return the
# next number greater than num using the same digits. For example: if num is 123 return 132, if it's 12453 return 12534.
#  If a number has no greater permutations, return -1 (ie. 999).

import itertools


def PermutationStep(num):
    perms = [int(''.join(perm)) for perm in itertools.permutations(str(num))]

    list_perms = list(set(perms))
    list_perms.sort()
    print list_perms

    num_index = list_perms.index(num)
    try:
        if list_perms[num_index + 1] > num:
            return list_perms[num_index + 1]
        return -1
    except IndexError:
        return -1

