#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    #strict type casting (personal preference)
    a = list(a)
    b = list(b)

    if 0 in a or 0 in b:
        return 0
    lcm = math.lcm(*a)
    print(lcm)

    result = 0
    count = 1
    while True:
        current_conditions = list((value %(lcm * count)) == 0 for value in b)
        print("lcm", lcm * count)
        print(current_conditions)
        if min(current_conditions):
            #All values are true
            result = result + 1
        elif not max(current_conditions):
            if (lcm * count) >= max(b):
                break;
        count = count + 1
    return result;

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    #fptr.write(str(total) + '\n')

    #fptr.close()
