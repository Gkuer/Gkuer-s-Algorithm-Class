import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    global ans

    visited[i] = True
    cycle.append(i)
    node = maps[i]

    if visited[node]:
        if node in cycle:
            ans += cycle[cycle.index(node):]
        return
    else:
        dfs(node)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)

    ans = []
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))

# Pass