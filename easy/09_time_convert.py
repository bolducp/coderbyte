# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the
# number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.

'''def CheckNums(num1,num2):
    if num1 == num2:
        return -1
    return num2 > num1'''



def TimeConvert(num):
    hour = num//60
    minutes = num%60
    if num==60:
        hour = 1
    return f"{hour}:{minutes}"
print(TimeConvert(int(input())))

    

