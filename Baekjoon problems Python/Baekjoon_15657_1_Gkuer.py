import sys
input = sys.stdin.readline

def find(x):
    if len(ans) >= m:
        print(*ans)
        return

    for i in range(x,n):
        ans.append(maps[i])
        find(i)
        ans.pop()

n, m = map(int,input().split())
maps = list(map(int,input().split()))
maps.sort()
ans = []
find(0)

# Pass