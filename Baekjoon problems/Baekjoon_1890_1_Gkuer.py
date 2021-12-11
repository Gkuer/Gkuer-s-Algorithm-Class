import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0)]

q = deque()
q.append([0,0])
temps = [[0] * n for _ in range(n)]
temps[n-1][n-1] = -1
cnt = 0

while q:
    idx, idy = q.popleft()
    for i in range(2):
        nr = idx + dirs[i][0]*maps[idx][idy]
        nc = idy + dirs[i][1]*maps[idx][idy]
        if 0 <= nr < n and 0 <= nc < n:
            if temps[nr][nc] == -1:
                temps[idx][idy] = -1
                cnt += 1
            else:
                q.append([nr,nc])

print(cnt)

# Fail: Time Over