import sys
input = sys.stdin.readline
from collections import deque

def bfs(idx):
    q = deque()
    q.append(idx)
    while q:
        now = q.popleft()
        for i in range(n):
            if not visited[i]:
                dist = (nodes[now][0] - nodes[i][0])**2 + (nodes[now][1] - nodes[i][1])**2
                if dist <= (nodes[now][2]+nodes[i][2])**2:
                    visited[i] = 1
                    q.append(i)

def go():
    global visited
    visited = [0] * (n)
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = []
    for i in range(n):
        a,b,c = map(int,input().split())
        nodes.append([a,b,c])

    print(go())

# Pass