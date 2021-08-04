#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    sqrt_a = math.floor(math.sqrt(a))
    sqrt_b = math.floor(math.sqrt(b))
    counter = 0
    
    for i in range(sqrt_a, sqrt_b + 1):
        if math.pow(i, 2) >= a and math.pow(i, 2) <= b:
            counter += 1
             
    return counter
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
