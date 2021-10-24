import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        idx, idy, who = q.popleft()
        for i in range(4):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < r and 0 <= nc < c:
                if maps[nr][nc] == ".":
                    if who == "w":
                        maps[nr][nc] = "w"
                        q.append([nr, nc, "w"])
                    elif who == "m":
                        if not visited[nr][nc]:
                            visited[nr][nc] = 1
                            maps[nr][nc] = maps[idx][idy] + 1
                            q.append([nr, nc, "m"])
                if nr == goal_idx and nc == goal_idy and who == "m":
                    print(maps[idx][idy])
                    return

    print("KAKTUS")
    return

r, c = map(int,input().split())
maps = [list(input().strip()) for _ in range(r)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[False]*c for _ in range(r)]
q = deque()
for i in range(r):
    for x in range(c):
        if maps[i][x] == "*":
            q.append([i,x,"w"])

for i in range(r):
    for x in range(c):
        if maps[i][x] == "S":
            q.append([i,x,"m"])
            maps[i][x] = 1
            visited[i][x] = 1
        elif maps[i][x] == "D":
            goal_idx, goal_idy = i, x

bfs()
# Pass