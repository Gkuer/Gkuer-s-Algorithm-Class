import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    global maps, part
    start = 0
    for i in range(n):
        for x in range(n):
            if maps[i][x] == '1':
                q = deque([[i,x]])
                while q:
                    if part.get(start):
                        part[start] += 1
                    else:
                        part[start] = 1
                    idx, idy = q.popleft()
                    for y in range(4):
                        nr = idx + dirs[y][0]
                        nc = idy + dirs[y][1]
                        if 0 <= nr < n and 0 <= nc < n:
                            if maps[nr][nc] == '1':
                                maps[nr][nc] = start
                                q.append([nr,nc])

                start += 1

n = int(input())
maps = [list(input().strip()) for _ in range(n)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
part = {}

BFS()
print(len(part))
ans = []
for i in part:
    if part[i]-1 == 0:
        part[i] = 2
    ans.append(part[i]-1)
ans = sorted(ans)
print(*ans, sep="\n")

# Pass