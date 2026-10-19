# p19 : Weighted Uniform Strings

# link : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

# code : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    prev_char = ''
    current_weight = 0

    for char in s:
        char_val = ord(char) - ord('a') + 1
        if char == prev_char:
            current_weight += char_val
        else:
            prev_char = char
            current_weight = char_val
        weights.add(current_weight)

    return ['Yes' if q in weights else 'No' for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
