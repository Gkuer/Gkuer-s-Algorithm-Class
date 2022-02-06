import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    maps = list(map(int,input().split()))
    print(sorted(maps)[-3])

# Pass