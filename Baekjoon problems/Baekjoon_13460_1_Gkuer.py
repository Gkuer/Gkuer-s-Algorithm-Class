import sys

input = sys.stdin.readline
from collections import deque


def go(idx, idy, i):
    cnt = 0
    while maps[idx + dirs[i][0]][idy + dirs[i][1]] != "#" and maps[idx][idy] != "O":
        idx += dirs[i][0]
        idy += dirs[i][1]
        cnt += 1
    return idx, idy, cnt


def bfs():
    while q:
        red_r, red_c, blue_r, blue_c, time = q.popleft()
        if time > 10:
            break

        for i in range(4): d
        red_nr, red_nc, red_cnt = go(red_r, red_c, i)
        blue_nr, blue_nc, blue_cnt = go(blue_r, blue_c, i)
        if maps[blue_nr][blue_nc] != "O":
            if maps[red_nr][red_nc] == "O":
                print(time)
                return
            if red_nr == blue_nr and red_nc == blue_nc:
                if red_cnt > blue_cnt:
                    red_nr -= dirs[i][0]
                    red_nc -= dirs[i][1]
                else:
                    blue_nr -= dirs[i][0]
                    blue_nc -= dirs[i][1]

            if not temps[red_nr][red_nc][blue_nr][blue_nc]:
                temps[red_nr][red_nc][blue_nr][blue_nc] = 1
                q.append([red_nr, red_nc, blue_nr, blue_nc, time + 1])


print(-1)

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
temps = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for x in range(m):
        if maps[i][x] == "R":
            rx, ry = i, x
        elif maps[i][x] == "B":
            bx, by = i, x

q = deque()
q.append([rx, ry, bx, by, 1])
temps[rx][ry][bx][by] = 1
bfs()

# Pass
