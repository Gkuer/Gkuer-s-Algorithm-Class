import sys
input = sys.stdin.readline

n, k = map(int,input().split())
maps = list(map(int,input().split()))
print(sorted(maps)[k-1])

# Pass