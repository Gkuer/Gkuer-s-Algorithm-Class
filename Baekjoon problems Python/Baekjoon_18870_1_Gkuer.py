import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

set_maps = sorted(list(set(maps)))
dict_maps = {set_maps[i]:i for i in range(len(set_maps))}

for i in maps:
    print(dict_maps[i],end=" ")

# Pass