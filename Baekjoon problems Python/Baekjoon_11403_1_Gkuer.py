import sys
from collections import deque
input = sys.stdin.readline

def find(idx,idy):
    visited = [0] * n
    q = deque([])
    q.append(idx)
    while q:
        pos = q.popleft()
        for i in range(n):
            if maps[pos][i] and not visited[i]:
                if i == idy:
                    return 1
                else:
                    visited[i] = 1
                    q.append(i)
    return 0

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

res = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        res[i][j] = find(i,j)

for i in range(n):
    print(*res[i])

# Pass