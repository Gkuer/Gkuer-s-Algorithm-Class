import sys
input = sys.stdin.readline

n = int(input())
maps = []
for _ in range(n):
    maps.append(input().strip())

maps = sorted(set(maps))
maps.sort(key = lambda x: len(x))

for i in range(len(maps)):
    print(maps[i])

# Pass