import sys
input = sys.stdin.readline
from collections import deque
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def check():
    for i in range(n):
        for x in range(m):
            if maps[i][x] != 0:
                return True
    return False

def bfs():
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for x in range(m):
            if maps[i][x] != 0 and not visited[i][x]:
                q.append([i,x])
                visited[i][x] = 1
                while q:
                    idx, idy = q.popleft()
                    for y in range(4):
                        nr = idx + dirs[y][0]
                        nc = idy + dirs[y][1]
                        if 0 <= nr < n and 0 <= nc < m:
                            if not visited[nr][nc] and maps[nr][nc] != 0:
                                q.append([nr,nc])
                                visited[nr][nc] = 1
                cnt += 1
    return cnt

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

time = 1
q = deque()
flag = False
while check():
    temps = [[0] * m for _ in range(n)]
    for i in range(n):
        for x in range(m):
            if maps[i][x] != 0:
                melt = 0
                for y in range(4):
                    nr = i + dirs[y][0]
                    nc = x + dirs[y][1]
                    if 0 <= nr < n and 0 <= nc < m:
                        if maps[nr][nc] == 0:
                             melt += 1
                temps[i][x] = melt

    for i in range(n):
        for x in range(m):
            if maps[i][x] != 0:
                maps[i][x] = maps[i][x] - temps[i][x]
                if maps[i][x] < 0:
                    maps[i][x] = 0

    if bfs() >= 2:
        print(time)
        flag = True
        break

    else:
        time += 1

if not flag:
    print(0)

# Pass