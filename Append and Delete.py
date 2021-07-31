#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    counter = 0
    flag = 0
    
    if s == t:
        return 'Yes'
    elif set(s) == set(t) and abs(len(s) - len(t)) + 2 == k:
        return 'Yes'
    else:
        if len(s) > len(t):
            length = len(s)
        else:
            length = len(t)
        for i in range(length):
            try:
                if s[i] == t[i] and flag == 0:
                    continue
                else:
                    counter += 2
                    flag = 1
            except:
                counter += 1
        if counter == k or k > (len(s) +len(t)):
            return 'Yes'
        else:
            print(str(counter) + 'length:' + str(len(s))) 
            return 'No'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
