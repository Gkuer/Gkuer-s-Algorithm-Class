import sys
input = sys.stdin.readline
from collections import deque

r, c, n = map(int,input().split())
maps = [[0]*c for _ in range(r)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(n):
    c1, r1, c2, r2 = map(int,input().split())
    lu_x, lu_y = r-r2, c1
    rd_x, rd_y = r-r1, c2
    for x in range(r):
        for y in range(c):
            if lu_x <= x < rd_x and lu_y <= y < rd_y:
                maps[x][y] = 1



ans_list = []
for i in range(r):
    for x in range(c):
        if maps[i][x] == 0:
            cnt = 0
            q = deque()
            q.append([i,x])
            maps[i][x] = 1
            while q:
                idx, idy = q.popleft()
                cnt += 1
                for y in range(4):
                    nr = idx + dirs[y][0]
                    nc = idy + dirs[y][1]
                    if 0 <= nr < r and 0 <= nc < c:
                        if maps[nr][nc] == 0:
                            q.append([nr,nc])
                            maps[nr][nc] = 1
            ans_list.append(cnt)

print(len(ans_list))
print(*sorted(ans_list))

# Pass