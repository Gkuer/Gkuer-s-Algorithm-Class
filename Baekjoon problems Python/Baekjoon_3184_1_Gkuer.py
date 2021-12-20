import sys

input = sys.stdin.readline
from collections import deque


def bfs(idx, idy):
    q.append([idx, idy])
    w, y = 0, 0
    if maps[idx][idy] == 'v':
        w += 1
    elif maps[idx][idy] == 'o':
        y += 1
    maps[idx][idy] = 'X'
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == '.':
                    q.append([nr, nc])
                    maps[nr][nc] = 'X'
                elif maps[nr][nc] == 'v':
                    w += 1
                    q.append([nr, nc])
                    maps[nr][nc] = 'X'
                elif maps[nr][nc] == 'o':
                    y += 1
                    q.append([nr, nc])
                    maps[nr][nc] = 'X'

    if w >= y:
        return w, 'w'
    else:
        return y, 'y'


n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()

wolf, yang = 0, 0
for i in range(n):
    for x in range(m):
        if maps[i][x] != '#' or maps[i][x] != 'X':
            cnt, flag = bfs(i, x)
            if flag == 'w':
                wolf += cnt
            else:
                yang += cnt

print(yang,wolf)

# Pass