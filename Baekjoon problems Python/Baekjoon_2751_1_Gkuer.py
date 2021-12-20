import sys
input = sys.stdin.readline

n = int(input())
maps = [int(input()) for _ in range(n)]

maps.sort()
for i in maps:
    print(i)

# Pass