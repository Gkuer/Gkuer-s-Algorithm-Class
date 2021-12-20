import sys
from collections import deque
import copy
input = sys.stdin.readline

def coloring(idx,idy, color):
    global q
    q.append([idx,idy])
    maps[idx][idy] = "O"
    while q:
        r, c = q.popleft()
        for y in range(4):
            nr = r + dirs[y][0]
            nc = c + dirs[y][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] == color:
                    q.append([nr,nc])
                    maps[nr][nc] = "O"

def jeokrok(idx, idy, color):
    global q
    q.append([idx,idy])
    maps2[idx][idy] = "O"
    while q:
        r, c = q.popleft()
        for y in range(4):
            nr = r + dirs[y][0]
            nc = c + dirs[y][1]
            if 0 <= nr < n and 0 <= nc < n:
                if color == "B":
                    if maps2[nr][nc] == "B":
                        q.append([nr,nc])
                        maps2[nr][nc] = "O"

                elif color == "R" or color == "G":
                    if maps2[nr][nc] == "R" or maps2[nr][nc] == "G":
                        q.append([nr,nc])
                        maps2[nr][nc] = "O"

n = int(input())
q = deque()
maps = [list(input().strip()) for _ in range(n)]
maps2 = copy.deepcopy(maps)
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

cnt = 0
cnt2 = 0
for i in range(n):
    for x in range(n):
        if maps[i][x] != "O":
            coloring(i,x,maps[i][x])
            cnt += 1
        if maps2[i][x] != "O":
            jeokrok(i,x,maps2[i][x])
            cnt2 += 1

print(cnt, cnt2)

# Pass