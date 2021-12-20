import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque([])
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            q.append([i,x])
            maps[i][x] = 1
while q:
    idx, idy = q.popleft()
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if maps[nr][nc] == 0:
                maps[nr][nc] = maps[idx][idy] + 1
                q.append([nr,nc])

flag = False
ans = 0
for i in range(n):
    for x in range(m):
        if maps[i][x] == 0:
            flag = True
        elif ans < maps[i][x]:
            ans = maps[i][x]

if flag:
    print(-1)
else:
    print(ans-1)

# Pass
