import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx,idy,road):
    q.append([idx,idy])
    visited = [[0]*c for _ in range(r)]
    visited[idx][idy] = 1
    while q:
        idx,idy = q.popleft()
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < r and 0 <= nc < c:
                if not visited[nr][nc] and road[nr][nc] == 0:
                    q.append([nr,nc])
                    visited[nr][nc] = 1
                    road[nr][nc] = road[idx][idy] + 1
    return road[r-1][c-1]

r, c = map(int,input().split())
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
maps = [list(map(int,input().strip())) for _ in range(r)]
q = deque()
ans = 9985489323
for i in range(r):
    for x in range(c):
        if maps[i][x] == 1:
            maps[i][x] = 0
            ans = min(ans, bfs(0,0,maps))
            maps[i][x] = 1

print(ans+1) if ans != 0 else print(-1)

# Fail: Time over