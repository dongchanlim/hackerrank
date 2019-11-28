'''
You are in charge of the cake for your niece's birthday
and have decided the cake will have one candle for each year of her total age.
When she blows out the candles, she’ll only be able to blow out the tallest ones.
Your task is to find out how many candles she can successfully blow out.
For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3,
she will be able to blow out 2 candles successfully,
since the tallest candles are of height 4 and there are 2 such candles
'''

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    count = ar.count(max(ar))
    return count
            
if __name__ == '__main__':

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(result)