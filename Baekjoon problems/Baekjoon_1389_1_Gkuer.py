import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,end):
    q = deque()
    q.append(start)
    cnt = 1
    visited = [0]*n
    visited[start] = 1
    while q:
        size = len(q)
        for z in range(size):
            now = q.popleft()
            for y in maps[now]:
                if y == end:
                    return cnt
                else:
                    if not visited[y]:
                        q.append(y)
                        visited[y] = 1
        cnt += 1

n, m = map(int,input().split())
maps = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    maps[a-1].append(b-1)
    maps[b-1].append(a-1)

ans = 129305813
for i in range(n):
    subans = 0
    for x in range(n):
        if i == x:
            continue
        else:
            subans += bfs(i,x)

    if ans > subans:
        ans = subans
        ans_idx = i

print(ans_idx+1)

# Pass