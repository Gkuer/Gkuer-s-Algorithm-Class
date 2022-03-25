import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))

maps.sort()
for map in maps:
    print(*map)

# Pass