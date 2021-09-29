import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(m)]
temps = [[0]*(n+1) for _ in range(n+1)]
for i, x in maps:
    temps[i][x] = temps[x][i] = 1


stack = []
cnt = 0
q = deque()
for i in range(1,n+1):
    if i in stack:
        continue

    q.append(i)
    while q:
        idx = q.popleft()
        for x in range(1,n+1):
            if temps[idx][x] and x not in stack:
                q.append(x)
                stack.append(x)

    cnt += 1

print(cnt)

# Pass