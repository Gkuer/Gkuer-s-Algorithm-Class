import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = [[] for _ in range(n+1)]
temps = [0]*(n+1)
for i in range(n-1):
    a, b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)
q = deque([1])
while q:
    now = q.popleft()
    for i in maps[now]:
        if temps[i] == 0:
            temps[i] = now
            q.append(i)

print(*temps[2:],sep="\n")
# Pass