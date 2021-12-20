import sys
from collections import deque
input = sys.stdin.readline

def DFS(v, already):
    already.append(v)
    print(v, end=" ")
    for w in range(n+1):
        if temps[v][w] and w not in already:
            DFS(w, already)

def BFS(v):
    q = deque([v])
    stack = [v]
    while q:
        v = q.popleft()
        print(v, end=" ")
        for w in range(n+1):
            if temps[v][w] and w not in stack:
                q.append(w)
                stack.append(w)

n, m, v = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(m)]
temps = [[False]*(n+1) for _ in range(n+1)]
for i, x in maps:
    temps[i][x] = temps[x][i] = True

DFS(v, [])
print()
BFS(v)

# Pass