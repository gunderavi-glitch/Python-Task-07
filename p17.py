# p17 : Separate the Numbers

# link : https://www.hackerrank.com/challenges/separate-the-numbers/problem

# code : 

import math
import os
import random
import re
import sys

def separateNumbers(s):
    if s.startswith('0') or len(s) < 2:
        print("NO")
        return

    n = len(s)
    for i in range(1, n // 2 + 1):
        first_num = int(s[:i])
        
        test_str = ""
        current = first_num
        while len(test_str) < n:
            test_str += str(current)
            current += 1
            
        if test_str == s:
            print(f"YES {first_num}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)
