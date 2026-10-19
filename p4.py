# p4 : Funny String

# link : https://www.hackerrank.com/challenges/funny-string/problem

# code : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    r = s[::-1]
    
    # Iterate through the string to compare absolute differences
    for i in range(1, len(s)):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        
        # If any difference doesn't match, it's not funny
        if diff_s != diff_r:
            return "Not Funny"
            
    # If all differences match
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
