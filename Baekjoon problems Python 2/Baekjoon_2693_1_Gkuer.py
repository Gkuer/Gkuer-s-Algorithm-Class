import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    maps = list(map(int,input().split()))
    maps.sort()
    print(maps[-3])

# Pass