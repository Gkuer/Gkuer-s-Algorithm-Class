import sys
from collections import deque
input = sys.stdin.readline
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs1(i,j,cnt):
    q = deque()
    q.append([i,j])
    maps[i][j] = cnt
    while q:
        idx, idy = q.popleft()
        for k in range(4):
            nr = idx + dirs[k][0]
            nc = idy + dirs[k][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = cnt
                    q.append([nr,nc])

def bfs2(x):
    global ans

    visited = [[0]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == x:
                q.append([i,j])

    while q:
        idx, idy = q.popleft()
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] == x:
                    continue
                if maps[nr][nc] == -1 and not visited[nr][nc]:
                    visited[nr][nc] = visited[idx][idy] + 1
                    q.append([nr,nc])
                elif maps[nr][nc] != -1 and maps[nr][nc] != x:
                    ans = min(visited[idx][idy], ans)
                    return


n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
cnt = 2

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0:
            maps[i][j] = -1
        elif maps[i][j] == 1:
            bfs1(i,j,cnt)
            cnt += 1

ans = 987654321
for i in range(2,cnt+2):
    bfs2(i)

print(ans)

# Pass