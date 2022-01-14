import sys
input = sys.stdin.readline

def perm(start):
    if len(maps) == m:
        print(*maps)
        return

    for i in range(start,n+1):
        if i not in maps:
            maps.append(i)
            perm(i+1)
            maps.pop()

n, m = map(int,input().split())
maps = []
perm(1)

# Pass