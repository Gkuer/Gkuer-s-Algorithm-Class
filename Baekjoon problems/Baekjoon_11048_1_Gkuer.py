import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(1,0),(0,1),(1,1)]

q = deque()
q.append([0,0,maps[0][0]])
temps = [[0 for _ in range(m)] for _ in range(n)]
while q:
    idx, idy, point = q.popleft()
    for i in range(3):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if temps[nr][nc] < (maps[nr][nc] + point):
                temps[nr][nc] = maps[nr][nc] + point
                q.append([nr,nc,maps[nr][nc]+point])

print(temps[n-1][m-1])

# Fail: Time Over