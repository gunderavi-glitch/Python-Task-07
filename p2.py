# p2 : The Captain's Room

# link : https://www.hackerrank.com/challenges/py-the-captains-room/problem

# code : 

k = int(input())
rooms = list(map(int, input().split()))
sum_unique_rooms = sum(set(rooms))
sum_all_rooms = sum(rooms)
captain_room = (sum_unique_rooms * k - sum_all_rooms) // (k - 1)
print(captain_room)
