#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    #Number Line Jumps
    #both starts at x1 and x2 respectively, v1 and v2 will be the increment. We have to assume that they arrive at position y after a certain interval. which means that x1 + (n1 * v1) = y and x2 + (n2 * v2) = y, so x1 + (n * y1) = x2 + (n *y2). (They have to arrive at the same time)
    #x1 - x2 = (n * y2) - (n * y1)
    #n = (y2 - y1)/ (x1 -x2)
    common_jump = float((v2 - v1)/ (x1 - x2))

    #we check if the value is integer
    #in case value is less than 1, we flip denominator and numerator
    #and we make sure it is positive integer
    return "YES" if (common_jump > 0 and (common_jump.is_integer() or (1/common_jump).is_integer())) else "NO"



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
