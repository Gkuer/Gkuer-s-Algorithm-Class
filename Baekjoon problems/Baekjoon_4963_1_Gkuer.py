import sys
from collections import deque
input = sys.stdin.readline
dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
q = deque()
while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for x in range(w):
            if maps[i][x] == 1:
                q.append([i,x])
                while q:
                    idx, idy = q.popleft()
                    for y in range(8):
                        nr = idx + dirs[y][0]
                        nc = idy + dirs[y][1]
                        if 0 <= nr < h and 0 <= nc < w:
                            if maps[nr][nc] == 1:
                                maps[nr][nc] = 0
                                q.append([nr,nc])
                cnt += 1

    print(cnt)

# Pass