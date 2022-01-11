import sys
from collections import deque
import math
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [0]*107
visited = [0]*107

for _ in range(n):
    s, g = map(int,input().split())
    maps[s] = g

for _ in range(m):
    s, g = map(int,input().split())
    maps[s] = g

q = deque([])
q.append([1,0])
ans = math.inf
while q:
    pos, cnt = q.popleft()

    if pos >= 100:
        ans = min(ans, cnt)

    else:
        for i in range(1,7):
            if not maps[pos+i]:
                next = pos + i
            else:
                next = maps[pos+i]

            if not visited[next]:
                q.append([next,cnt+1])
                visited[next] = 1

print(ans)

# Pass