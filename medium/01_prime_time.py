# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is
# a prime number, otherwise return the string false. The range will be between 1 and 2^16.

import math

def PrimeTime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        if num % 2 == 0:
            return False
        else:
            for potential_factor in range(3, int(math.sqrt(num) + 1), 2):
                if num % potential_factor == 0:
                    return False
    return True


# keep this function call here
# to see how to enter arguments in Python scroll down
print PrimeTime(int(raw_input()))
