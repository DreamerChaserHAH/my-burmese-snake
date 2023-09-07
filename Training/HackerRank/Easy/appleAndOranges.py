#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    #a = apple tree location
    #b = orange tree location
    #s = house point 1
    #t = house point 2
    #apples = apple list and their drop distance
    #oranges = orange list and their drop distance
    def is_in_range(point):
        return point >= s and point <= t

    #Using List Comprehension
    #Find Apple
    print(len(list(filter(is_in_range, 
                          [(a + distance) for distance in apples]))))
    #Find Oranges 
    print(len(list(filter(is_in_range, 
                          [(b + distance) for distance in oranges]))))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
