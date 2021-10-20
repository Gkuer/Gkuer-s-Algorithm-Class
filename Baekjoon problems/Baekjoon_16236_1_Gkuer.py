import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx, idy, status):
    q = deque()
    q.append([idx,idy])
    temps = [[0]*n for _ in range(n)]
    temps[idx][idy] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if not temps[nr][nc] and maps[nr][nc] <= status:
                    q.append([nr,nc])
                    temps[nr][nc] = temps[r][c] + 1

    mx = 9494949443
    subans = []
    for i in range(n):
        for x in range(n):
            if maps[i][x] != 0 and temps[i][x] < mx and maps[i][x] < status and temps[i][x] != 0:
                mx = temps[i][x]
                subans = [[i,x]]
            elif maps[i][x] != 0 and temps[i][x] == mx and maps[i][x] < status and temps[i][x] != 0:
                subans.append([i,x])

    if subans:
        return sorted(subans)[0] + [mx-1]
    else:
        return False


n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(n):
    for x in range(n):
        if maps[i][x] == 9:
            start_idx, start_idy = i, x
            maps[i][x] = 0

status = 2
status_cnt = status
ans = 0
while True:
    res = bfs(start_idx, start_idy, status)
    if res:
        res_r, res_c, mx = res
        maps[res_r][res_c] = 0
        start_idx, start_idy = res_r, res_c
        status_cnt -= 1
        ans += mx
        if status_cnt == 0:
            status += 1
            status_cnt = status
    else:
        break

print(ans)

# Pass