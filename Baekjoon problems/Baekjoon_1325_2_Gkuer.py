import sys

input = sys.stdin.readline
from collections import deque


def dfs(idx):
    q.append(idx)
    visited = [False] * (n + 1)
    cnt = 0
    while q:
        now = q.pop()
        for x in range(1, n + 1):
            if now in maps[x] and not visited[x]:
                visited[x] = 1
                q.append(x)
                cnt += 1
    return cnt


n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
q = deque()
for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)

mx = 0
for i in range(1, n + 1):
    a = dfs(i)
    if mx < a:
        mx = a
        ans = [i]
    elif mx == a:
        ans.append(i)
print(*ans)

# Fail: Time Over