import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

print(*sorted(list(set(maps))))

# Pass