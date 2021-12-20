import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx):
    q.append(idx)
    visited = [0] * (n+1)
    visited[idx] = 1
    cnt =0
    while q:
        now = q.popleft()
        for i in maps[now]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)

    return cnt

n, m = map(int,input().split())
maps = [[] for _ in range(n+1)]
q = deque()
for _ in range(m):
    a, b = map(int,input().split())
    maps[b].append(a)

mx = -1
for i in range(1, n+1):
    a = bfs(i)
    if a > mx:
        mx = a
        ans = [i]
    elif a == mx:
        ans.append(i)

print(*ans)

# Pass