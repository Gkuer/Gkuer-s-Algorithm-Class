import sys
input = sys.stdin.readline
from collections import deque

def dfs(start,cnt):
    if cnt >= 5:
        return 1

    for i in maps[start]:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i,cnt+1)
            if res:
                return 1
            else:
                visited[i] = 0
    return 0

def go():
    for i in range(n):
        visited[i] = 1
        if dfs(i,1):
            return 1
        visited[i] = 0

    return 0

n, m = map(int,input().split())
maps = [[] for _ in range(n)]
q = deque()
for _ in range(m):
    a, b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)

visited = [0] * n
print(go())

# Pass


