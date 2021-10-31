import sys
input = sys.stdin.readline
from collections import deque

def dfs(idx,idy):
    q.append([idx,idy])
    maps[idx][idy] = 0
    cnt = 1
    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = 0
                    q.append([nr,nc])
                    cnt += 1

    return cnt

n, m, k = map(int,input().split())
maps = [[0]*m for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
for _ in range(k):
    a, b = map(int,input().split())
    maps[a-1][b-1] = 1

mx = 0
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            mx = max(mx,dfs(i,x))


print(mx)

# Pass