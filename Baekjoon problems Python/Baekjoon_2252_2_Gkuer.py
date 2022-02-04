import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [0] * 32001
graph = [[] for _ in range(32001)]
q = deque()

for _ in range(m):
    a, b = map(int,input().split())
    maps[b] += 1
    graph[a].append(b)

for i in range(1,n+1):
    if not maps[i]:
        q.append(i)

while q:
    pos = q.popleft()

    for i in graph[pos]:
        maps[i] -= 1
        if not maps[i]:
            q.append(i)

    print(pos, end=" ")

for i in range(1,n+1):
    if maps[i]:
        print("circulation")
        break
        
# Pass