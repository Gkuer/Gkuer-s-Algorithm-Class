import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append([s,0])
    while q:
        now, cnt = q.popleft()
        if now == g:
            return cnt

        if not visited[now]:
            visited[now] = 1
            if now+u <= f:
                q.append([now+u,cnt+1])
            if now-d >= 1:
                q.append([now-d,cnt+1])

    return "use the stairs"

f, s, g, u, d = map(int,input().split())
visited = [0]*1000001
ans = 0
print(bfs())

# Pass