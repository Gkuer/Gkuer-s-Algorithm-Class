import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx,idy):
    q.append([idx,idy])
    visited = [[0]*m for _ in range(n)]
    visited[idx][idy] = 1
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                    cnt += 1
    return cnt

n, m = map(int,input().split())
maps = [list(map(lambda x: int(x),input().strip())) for _ in range(n)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            maps[i][x] = bfs(i,x) % 10

for i in maps:
    print(*i,sep="")

# Fail: Time Over