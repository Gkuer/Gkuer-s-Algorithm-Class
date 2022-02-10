import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))
maps.sort()

print(maps[0]*maps[-1])

# Pass