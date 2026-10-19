# p15 : Game of Thrones - I

# link : https://www.hackerrank.com/challenges/game-of-thrones/problem

# code : 

import os
from collections import Counter

# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    counts = Counter(s)
    odd_count = sum(1 for freq in counts.values() if freq % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
