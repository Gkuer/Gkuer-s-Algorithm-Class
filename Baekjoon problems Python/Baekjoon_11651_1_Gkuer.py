import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

maps.sort(key=lambda x: (x[1],x[0]))
for i, x in maps:
    print(i, x)

# Pass