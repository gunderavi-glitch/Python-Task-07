# p3 : Mars Exploration

# link : https://www.hackerrank.com/challenges/mars-exploration/problem

# code : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    changed = 0
    # The expected pattern is "SOS" repeating
    expected_pattern = "SOS"
    
    for i in range(len(s)):
        # Compare each character in the string to the expected character
        if s[i] != expected_pattern[i % 3]:
            changed += 1
            
    return changed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
