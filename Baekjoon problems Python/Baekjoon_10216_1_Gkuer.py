import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx, idy):
    q = deque()
    q.append([idx,idy])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < 5001 and 0 <= nc < 5001:
                if maps[nr][nc]:
                    maps[nr][nc] = 0
                    q.append([nr,nc])

t = int(input())
for tc in range(t):
    n = int(input())
    maps = [[0]*5001 for _ in range(5001)]
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for i in range(n):
        r, c, d = map(int,input().split())
        maps[r][c] = 1
        for x in range(d):
            for y in range(4):
                nr = r + dirs[y][0]*(x+1)
                nc = c + dirs[y][1]*(x+1)
                if 0 <= nr < 5001 and 0 <= nc < 5001:
                    if not maps[nr][nc]:
                        maps[nr][nc] = 1

    cnt = 0
    for i in range(5001):
        for x in range(5001):
            if maps[i][x] == 1:
                bfs(i,x)
                cnt += 1

    print(cnt)

# Fail: TimeOver