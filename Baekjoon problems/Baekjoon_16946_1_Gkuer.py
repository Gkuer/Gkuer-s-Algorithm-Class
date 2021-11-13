import sys
input = sys.stdin.readline
from collections import deque

def dfs_dp(idx,idy):
    q.append([idx,idy])
    visited[idx][idy] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                    cnt += 1

    temps[idx][idy] = cnt

n, m = map(int,input().split())
maps = [list(map(int,list(input().strip()))) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            maps[i][x] = -1

q = deque()
temps = [[0]*m for _ in range(n)]
for i in range(n):
    for x in range(m):
        if maps[i][x] == 0:
            visited = [[0] * m for _ in range(n)]
            dfs_dp(i,x)

ans = [[0]*m for _ in range(n)]
for i in range(n):
    for x in range(m):
        if maps[i][x] == -1:
            ans[i][x] = 1
            for y in range(4):
                nr = i + dirs[y][0]
                nc = x + dirs[y][1]
                if 0 <= nr < n and 0 <= nc < m:
                    if temps[nr][nc] != -1:
                        ans[i][x] += temps[nr][nc]

            ans[i][x] %= 10


for i in ans:
    print(*i,sep="")

# Fail: Time Over