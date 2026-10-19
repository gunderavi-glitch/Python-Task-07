# p6 : Pangrams

# link : https://www.hackerrank.com/challenges/pangrams/problem

# code :

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Convert the input string to lowercase and convert it to a set
    # Check if the alphabet set is a subset of the characters in the string
    if alphabet.issubset(set(s.lower())):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
