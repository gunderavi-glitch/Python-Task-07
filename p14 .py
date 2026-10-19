# p14 : Anagram

# link : https://www.hackerrank.com/challenges/anagram/problem

# code :

import os

def anagram(s):
    # An anagram pair is impossible if length is odd
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    count1 = {}
    count2 = {}
    
    for ch in s1:
        count1[ch] = count1.get(ch, 0) + 1
    for ch in s2:
        count2[ch] = count2.get(ch, 0) + 1
        
    changes = 0
    for ch, count in count1.items():
        if count > count2.get(ch, 0):
            changes += count - count2.get(ch, 0)
            
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
