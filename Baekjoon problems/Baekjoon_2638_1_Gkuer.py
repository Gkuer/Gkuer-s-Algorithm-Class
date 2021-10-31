import sys
input = sys.stdin.readline
from collections import deque

def check():
    for i in range(r):
        for x in range(c):
            if maps[i][x] == 1:
                return True
    return False

def bfs(idx,idy):
    q.append([idx,idy])
    visited[idx][idy] = 1
    while q:
        now_r, now_c = q.popleft()
        for i in range(4):
            nr = now_r + dirs[i][0]
            nc = now_c + dirs[i][1]
            if 0 <= nr < r and 0 <= nc < c:
                if maps[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                elif maps[nr][nc] == 1:
                    visited[nr][nc] += 1

r, c = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(r)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
time = 0
while check():
    visited = [[0]*c for _ in range(r)]
    bfs(0,0)

    for i in range(r):
        for x in range(c):
            if visited[i][x] >= 2:
                maps[i][x] = 0

    time += 1

print(time)

# Pass
