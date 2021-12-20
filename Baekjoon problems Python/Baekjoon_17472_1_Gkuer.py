import copy
import sys
input = sys.stdin.readline
from collections import deque

def dfs(idx,idy,flag):
    maps[idx][idy] = flag
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if maps[nr][nc] == 1 and not temps[nr][nc]:
                temps[nr][nc] = 1
                maps[nr][nc] = flag
                dfs(nr,nc,flag)

def straight(x1, y1, d, p, acheck):
    t = 1
    acheck[x1][y1] = 1
    while maps[x1][y1] == 0:
        acheck[x1][y1] = 1
        p += 1
        x1 += dirs[d][0]
        y1 += dirs[d][1]
        if 0 <= x1 < n and 0 <= y1 < m:
            pass
        else:
            t = 0 # t 0: 갈곳 없음, 1: 땅에 도착
            break
    # print(*acheck, sep="\n")
    # print(p)
    # print()
    return x1, y1, p, t, acheck

def check(li):
    for i in range(1,cnt+1):
        if li[i] == 0:
            return 0
    return 1

def go(idx,idy):
    ans = 100000000
    q = deque()
    temps = [0]*(cnt+1)
    temps[maps[idx][idy]] = 1
    visited = [[0]*m for _ in range(n)]
    visited[idx][idy] = 1
    checking = [[0]*m for _ in range(n)]
    q.append([idx,idy, 0, 1, temps, visited,checking])
    while q:
        r, c, point, tag, current,already,checking = q.popleft()
        if check(current):
            print(*checking,sep="\n")
            print(point)
            ans = min(ans,point)
            continue

        already[r][c] = 1
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if already[nr][nc] == 0:
                    if maps[nr][nc] == 0:
                        checking2 = copy.deepcopy(checking)
                        x, y, p, t, checking2 = straight(nr,nc,i, 0, checking2)

                        if t == 0:
                            continue

                        if current[maps[x][y]] == 1:
                            continue

                        if p <= 1:
                            continue

                        current2 = copy.deepcopy(current)
                        current2[maps[x][y]] = 1
                        q.append([x,y,point+p, tag + 1,current2, already, checking2])
                        for i in range(4):
                            nr = r + dirs[i][0]
                            nc = c + dirs[i][1]
                            if 0 <= nr < n and 0 <= nc < m:
                                if maps[nr][nc] != 0:
                                    q.append([nr, nc, point + p, tag + 1, current2, already, checking2])
                    else:
                        q.append([nr,nc,point,tag,current, already,checking])


    if ans == 100000000:
        return -1
    return ans

def base():
    for i in range(n):
        for x in range(m):
            if maps[i][x] == 1:
                return go(i, x)


n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

temps = [[0]*m for _ in range(n)]
cnt = 1
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1 and temps[i][x] == 0:
            dfs(i,x,cnt)
            cnt += 1

cnt -= 1
print(base())

# Fail: Wrong answer