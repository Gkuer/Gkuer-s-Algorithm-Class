import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

maps_dict = {}
for i in maps:
    if i in maps_dict:
        maps_dict[i] += 1
    else:
        maps_dict[i] = 1

m = int(input())
arr = list(map(int,input().split()))

for i in arr:
    if i in maps_dict:
        print(maps_dict[i],end=" ")
    else:
        print(0,end=" ")

# Pass