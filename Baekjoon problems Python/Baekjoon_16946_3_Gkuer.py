import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx,idy,flag):
    q.append([idx,idy])
    visited[idx][idy] = 1
    temps = [[idx,idy]]
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                    cnt += 1
                    temps.append([nr,nc])

    for i, x in temps:
        visited[i][x] = [cnt,flag]

n, m = map(int,input().split())
maps = [list(map(lambda x: int(x),input().strip())) for _ in range(n)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()

visited = [[0] * m for _ in range(n)]
flag = 0
for i in range(n):
    for x in range(m):
        if maps[i][x] == 0 and visited[i][x] == 0:
            bfs(i,x,flag)
            flag += 1

for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            temp = 1
            already = []
            for y in range(4):
                nr = i + dirs[y][0]
                nc = x + dirs[y][1]
                if 0 <= nr < n and 0 <= nc < m:
                    if maps[nr][nc] == 0:
                        for z in already:
                            if z[1] == visited[nr][nc][1]:
                                break
                        else:
                            temp += visited[nr][nc][0]
                            already.append(visited[nr][nc])

            maps[i][x] = str(temp % 10)

for i in maps:
    print(*i,sep="")

# Pass