import sys
input = sys.stdin.readline
from collections import deque

def bfs(i):
    q.append([i,2])
    temps[i] = 1
    while q:
        now, flag = q.popleft()
        visited[now] = 1
        for x in lines[now]:
            if not temps[x]:
                temps[x] = flag
                if not visited[x]:
                    if flag == 1:
                        q.append([x,2])
                    else:
                        q.append([x,1])
            else:
                if flag != temps[x]:
                    return False
                else:
                    if not visited[x]:
                        if flag == 1:
                            q.append([x,2])
                        else:
                            q.append([x,1])
    return True

t = int(input())
for tc in range(1,t+1):
    v, e = map(int,input().split())
    visited = [0]*(v+1)
    temps = [0]*(v+1)
    lines = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int,input().split())
        lines[a].append(b)
        lines[b].append(a)

    q = deque()
    for i in range(1,v+1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                break
    else:
        print("YES")
# Pass
