import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    global real_maps
    real_maps[0][0] = 2
    q = deque([[0, 0]])
    while q:
        idx, idy = q.popleft()
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if real_maps[nr][nc] == 1:
                    real_maps[nr][nc] = real_maps[idx][idy] + 1
                    q.append([nr,nc])

n, m = map(int, input().split())
maps = [input().strip() for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
real_maps=[]
for i in maps:
    temps = []
    for x in i:
        temps.append(int(x))
    real_maps.append(temps)

r, c = n-1, m-1

BFS()
print(real_maps[r][c]-1)

# Pass