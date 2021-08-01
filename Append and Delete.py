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
    
    #Case 1
    if s == t:
        return 'Yes'
    
    #Case 2
    elif set(s) == set(t) and abs(len(s) - len(t)) + 2 == k:
        return 'Yes'
    #Case 3
    else:
        #We need to go to the end of the longest string. That is why we are taking the maximum length between two strings.
        if len(s) > len(t):
            length = len(s)
        else:
            length = len(t)
        #We need to compare each letter of the two strings index wise.
        for i in range(length):
        #We need to use a try except block here because the length of the two strings is not equal.
        #If the letters of the two strings are equal for the same location then we do not need to do anything.
        #We are taking a flag here because we need to continue until the substring of both the strings is same. Here the substring starts from the beginning of the string.
            try:
                if s[i] == t[i] and flag == 0:
                    continue
        #If the letters are not equal then we need to add 2 to the counter. One for delete and one for append.
                else:
                    counter += 2
                    flag = 1
        #We need to add 1 to the counter for each letter of the rest of the longest string. This is for the deletion.
            except:
                counter += 1
        #If the counter is equal to k or k is greater than the sum of the length of the two strings then we return a 'Yes'. We return 'Yes' if k is greater than the sum of the length of two strings because we can waste extra moves by deletion. By doing multiple deletions we will get an empty string. 
        if counter == k or k > (len(s) +len(t)):
            return 'Yes'
        else:
            return 'No'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
