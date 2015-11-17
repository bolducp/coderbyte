# Have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases,
# the parameter num will be any number from 1 to 1000.

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def SimpleAdding(num):
    total = 0
    for each_num in xrange(num + 1):
        total += each_num
    return total

# keep this function call here
# to see how to enter arguments in Python scroll down
print SimpleAdding(int(raw_input()))