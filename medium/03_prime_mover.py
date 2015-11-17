# Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4.
# For example: if num is 16 the output should be 53 as 53 is the 16th prime number.

import math


def PrimeMover(num):
    primes = get_primes()
    return primes[num - 1]


def get_primes():
    primes = [2]
    for num in xrange(3, 1000):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(num):
    for potential_factor in xrange(2, int(math.sqrt(num) + 1)):
        if num % potential_factor == 0:
            return False
    return True
