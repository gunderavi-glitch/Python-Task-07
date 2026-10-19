# p13 : Sherlock and the Valid String

# link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# code : 

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    char_counts = Counter(s)
    freq_counts = Counter(char_counts.values())
    
    # Case 1: All characters have the same frequency
    if len(freq_counts) == 1:
        return "YES"
    
    # If there are more than 2 distinct frequencies, it's impossible to fix in 1 removal
    if len(freq_counts) > 2:
        return "NO"
    
    # Case 2: Exactly two distinct frequencies
    (f1, c1), (f2, c2) = freq_counts.items()
    
    # Ensure (f1, c1) is the one with smaller frequency
    if f1 > f2:
        f1, c1, f2, c2 = f2, c2, f1, c1
        
    # Subcase 2a: One character appears only once (freq 1, count 1)
    # e.g., {'a': 1, 'b': 2, 'c': 2} -> removing 'a' leaves all 2s
    if f1 == 1 and c1 == 1:
        return "YES"
        
    # Subcase 2b: The larger frequency is exactly 1 greater and occurs only once
    # e.g., {'a': 2, 'b': 2, 'c': 3} -> removing one 'c' reduces it to 2
    if f2 - f1 == 1 and c2 == 1:
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)
