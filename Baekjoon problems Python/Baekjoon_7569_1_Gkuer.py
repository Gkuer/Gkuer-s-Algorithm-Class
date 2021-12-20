import sys
input = sys.stdin.readline
from collections import deque

c, r, h = map(int,input().strip().split())
maps = [list(map(int,input().strip().split())) for _ in range(r*h)]
ans = 0
dirs = [(0,1,0),(1,0,0),(-1,0,0),(0,-1,0),(0,0,r),(0,0,-r)]

def checking():
    for i in range(r*h):
        for x in range(c):
            if maps[i][x] == 0:
                return False
    else:
        return True

# Originally Ended
if checking():
    ans = 0

# Go logic
else:
    q = deque()
    for i in range(r*h):
        for x in range(c):
            if maps[i][x] == 1:
                q.append([i,x])

    while q:
        idx, idy = q.popleft()
        for i in range(6):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            nh = dirs[i][2]
            if nh == 0:
                if (idx//r)*r <= nr < r*(idx//r+1) and 0 <= nc < c:
                    if maps[nr][nc] == 0:
                        maps[nr][nc] = maps[idx][idy] + 1
                        q.append([nr,nc])
            else: # Heghit is on
                nr = nr + nh
                nc = nc
                if 0 <= nr < r*h and 0 <= nc < c:
                    if maps[nr][nc] == 0:
                        maps[nr][nc] = maps[idx][idy] + 1
                        q.append([nr,nc])
        # print(*maps,sep="\n",end="\n--------\n")

    if not checking():
        ans = -1
    else:
        mx = 0
        for i in range(r*h):
            for x in range(c):
                if maps[i][x] > mx:
                    mx = maps[i][x]
        ans = mx-1

print(ans)
# Pass