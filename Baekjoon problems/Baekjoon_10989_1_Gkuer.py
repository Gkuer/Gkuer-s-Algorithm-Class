import sys
input = sys.stdin.readline

n = int(input())
maps = {}
for i in range(n):
    n = int(input())
    if maps.get(n):
        maps[n] += 1
    else:
        maps[n] = 1

maps = sorted(maps.items(), key=lambda x: x[1])
for key,value in maps:
    for j in range(value):
        print(key)

# Pass