import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx, idy, union):
    q = deque()
    q.append([idx,idy])
    sub_res = []
    temps[idx][idy] = 1
    while q:
        r, c = q.popleft()
        sub_res.append([r,c,maps[r][c]])
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if left <= abs(maps[r][c]-maps[nr][nc]) <= right:
                    if not temps[nr][nc]:
                        temps[nr][nc] = union
                        q.append([nr,nc])

    if len(sub_res) >= 2:
        return sub_res
    else:
        return False

def go():
    global temps
    time = 0
    while True:
        union = 1
        subans = []
        temps = [[0] * n for _ in range(n)]
        flag = False
        for i in range(n):
            for x in range(n):
                if not temps[i][x]:
                    res = bfs(i,x,union)
                    if res:
                        subans.append(res)
                        flag = True
        if not flag:
            return time

        for i in range(len(subans)):
            sm = 0
            for y in range(len(subans[i])):
                sm += subans[i][y][2]
            val = sm//len(subans[i])
            for y in range(len(subans[i])):
                maps[subans[i][y][0]][subans[i][y][1]] = val

        time += 1


n, left, right = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
print(go())

# Pass