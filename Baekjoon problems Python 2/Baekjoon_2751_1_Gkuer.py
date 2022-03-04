import sys
input = sys.stdin.readline

n = int(input())

maps = []
for _ in range(n):
    maps.append(int(input()))

maps.sort()
for i in range(n):
    print(maps[i])

# Pass