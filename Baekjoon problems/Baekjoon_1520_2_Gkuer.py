import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
cnt = 0
q = deque()
q.append([0,0])
while q:
    idx, idy = q.pop()
    if idx == n-1 and idy == m-1:
        cnt += 1

    else:
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] < maps[idx][idy]:
                    q.append([nr,nc])
print(cnt)

# Fail: Time Over