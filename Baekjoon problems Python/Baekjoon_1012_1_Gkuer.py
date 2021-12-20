import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    cnt = 0
    for i in range(n):
        for x in range(m):
            if temps[i][x] == -2:
                q = deque([[i,x]])
                cnt += 1
                while q:
                    idx, idy = q.popleft()
                    for y in range(4):
                        nr = idx + dirs[y][0]
                        nc = idy + dirs[y][1]
                        if 0 <= nr < n and 0 <= nc <m:
                            if temps[nr][nc] == -2:
                                temps[nr][nc] = 1
                                q.append([nr,nc])
    return cnt

t = int(input())
for tc in range(1,t+1):
    m, n, k = map(int,input().split())
    temps = [[-1]*m for _ in range(n)]
    maps = [list(map(int,input().split())) for _ in range(k)]
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for r, c in maps:
        temps[c][r] = -2

    print(BFS())

# Pass