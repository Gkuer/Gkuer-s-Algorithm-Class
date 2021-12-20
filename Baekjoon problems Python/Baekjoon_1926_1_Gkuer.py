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
                    cnt +=  1
                    q.append([nr,nc])
    return cnt

n, m = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
q = deque()
picture = 0
picture_mx = 0
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            res = dfs(i,x)
            if res > picture_mx:
                picture_mx = res
            picture += 1

print(picture)
print(picture_mx)

# Pass