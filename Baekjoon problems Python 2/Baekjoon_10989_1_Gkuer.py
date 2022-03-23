import sys
input = sys.stdin.readline

n = int(input())
maps = {}
for i in range(n):
    data = int(input())
    if data in maps:
        maps[data] += 1
    else:
        maps[data] = 1

for i in sorted(maps.keys()):
    for j in range(maps[i]):
        print(i)

# Pass