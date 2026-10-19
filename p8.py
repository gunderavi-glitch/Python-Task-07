# p8 : Gemstones

# link : https://www.hackerrank.com/challenges/gem-stones/problem

# code :

def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common = common.intersection(set(rock))

    return len(common)


n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

print(gemstones(arr))
