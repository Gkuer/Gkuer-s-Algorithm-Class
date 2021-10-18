import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s, g = map(int,input().split())
m = int(input())
maps = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)

q = deque()
q.append([s,0])
visited = [0]*(n+1)
ans = 0
while q:
    now, point = q.popleft()
    if now == g:
        ans = point
    for i in maps[now]:
        if not visited[i]:
            q.append([i, point+1])
            visited[i] = 1

print(ans) if ans != 0 else print(-1)

# Pass