import sys
input = sys.stdin.readline

def find(x):
    if len(maps) == m:
        print(*maps)
        return

    for i in range(x,n+1):
        maps.append(i)
        find(i)
        maps.pop()

n, m = map(int,input().split())
maps = []
find(1)

# Pass