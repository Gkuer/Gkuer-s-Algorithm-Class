import sys
input = sys.stdin.readline

n = int(input())
maps = list()
for i in range(n):
    maps.append(list(map(int,input().split())))

maps.sort(key=lambda x: (x[1],x[0]))

for map in maps:
    print(*map)

# Pass