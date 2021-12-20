import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maps = [[0]*n for _ in range(n)]
    start = list(map(int,input().split()))
    goal = list(map(int,input().split()))
    dirs = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

    q = deque()
    q.append(start)
    maps[start[0]][start[1]] = 1
    while q:
        idx, idy = q.popleft()
        for i in range(8):
            nr = idx + dirs[i][0]
            nc = idy + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] == 0:
                    maps[nr][nc] = maps[idx][idy]+1
                    q.append([nr,nc])

    print(maps[goal[0]][goal[1]]-1)
# Pass