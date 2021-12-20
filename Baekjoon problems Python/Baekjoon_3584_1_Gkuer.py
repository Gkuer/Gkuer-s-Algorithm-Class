import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def dfs2(now):

    if now not in visited:
        return dfs2(maps[now])

    else:
        for i in range(len(visited)):
            if visited[i] == now:
                return visited[i]

def dfs(now):
    if now == 0:
        return

    if now in visited:
        return

    visited.append(now)
    return dfs(maps[now])

t = int(input())
for tc in range(t):
    n = int(input())
    maps = [0] + [0]*n
    for _ in range(n-1):
        a, b = map(int,input().split())
        maps[b] = a

    x, y = map(int,input().split())

    visited = []
    dfs(x)

    print(dfs2(y))

# Pass