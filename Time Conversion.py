import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[:2])
    rest = s[2:-2]
    meridiem = s[-2:]
    if meridiem == "PM":
        if hour == 12:
            result = str(hour) + rest
        else:
            hour += 12
            result = str(hour) + rest
    else:
        if hour == 12:
            hour = "00"
            result = hour + rest
        else:
            if hour < 10:
                result = "0" + str(hour) + rest
            else:
                result = str(hour) + rest     
    return result

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)


