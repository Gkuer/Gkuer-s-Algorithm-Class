import sys
input = sys.stdin.readline
from collections import deque

def dfs(idx, idy, flag, temps):
    global ans

    if sum(flag) >= 7:
        if flag[0] >= 4:
            print(flag)
            print(*temps,sep="\n")
            print()
            ans += 1
        return

    if flag[1] >= 4:
        return

    for i in range(3):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            if not temps[nr][nc]:
                if maps[nr][nc] == "S":
                    flag[0] += 1
                    temps[nr][nc] = 1
                    dfs(nr, nc, flag, temps)
                    flag[0] -= 1
                    temps[nr][nc] = 0
                else:
                    flag[1] += 1
                    temps[nr][nc] = 1
                    dfs(nr, nc, flag, temps)
                    temps[nr][nc] = 0
                    flag[1] -= 1


maps = [list(input()) for _ in range(n)]
dirs = [(0,1),(1,0),(0,-1)]
visited = [[0]*n for _ in range(n)]
q = deque()
tag = [0,0]
ans = 0
for i in range(n):
    for x in range(n):
        if maps[i][x] == "S":
            tag[0] += 1
            visited[i][x] = 1
            dfs(i, x, tag, visited)  # S, Y
            visited[i][x] = 0
            tag[0] -= 1
        else:
            tag[1] += 1
            visited[i][x] = 1
            dfs(i, x, tag, visited)  # S, Y
            visited[i][x] = 0
            tag[1] -= 1


print(ans)

# Fail: Wrong Answer