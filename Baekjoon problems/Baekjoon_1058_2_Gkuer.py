import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx, idy):
    q = deque()
    q.append([idx,idy,1])
    while q:
        r, c, cnt = q.popleft()
        if cnt >= 3:
            break

        if cnt < visited[c]:
            visited[c] = cnt

        for i in range(n):
            if i != r and maps[c][i] == "Y":
                q.append([r,i,cnt+1])

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))


ans = 0
for i in range(n):
    visited = [100]*n
    cnt = 0
    for x in range(n):
        if maps[i][x] == "Y" and i != x:
            visited[x] = 1
            bfs(i,x)

    for i in range(n):
        if visited[i] <= 2:
            cnt += 1
    ans = max(ans,cnt)

print(ans)