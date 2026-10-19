# p10 : CamelCase

# link : https://www.hackerrank.com/challenges/camelcase/problem

# code : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    count = 1
    
    # Iterate through each character in the string
    for char in s:
        # If the character is uppercase, it indicates a new word
        if char.isupper():
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
