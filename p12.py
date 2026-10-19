# p12 : Making Anagrams

# link : https://www.hackerrank.com/challenges/making-anagrams/problem

# code : 

import os
from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    # Sum of absolute differences for each character frequency
    all_keys = set(c1.keys()).union(set(c2.keys()))
    return sum(abs(c1[char] - c2[char]) for char in all_keys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')
    fptr.close()
