import sys
from collections import deque
input = sys.stdin.readline

def fill_zero(x):
    required = 4 - len(x)
    return required*"0" + x

def bfs(n):
    q = deque()
    q.append([n,""])
    visited = [0]*10001
    visited[int(n)] = 1
    while q:
        now, record = q.popleft()

        if now == g:
            print(record)
            return

        # D
        value_d = int(now)*2
        if value_d > 9999:
            value_d = value_d % 10000
        if not visited[value_d]:
            visited[value_d] = 1
            q.append([fill_zero(str(value_d)), record+"D"])

        # S
        value_s = int(now) - 1
        if value_s == -1:
            value_s = 9999
        if not visited[value_s]:
            visited[value_s] = 1
            q.append([fill_zero(str(value_s)), record+"S"])

        # L
        value_l = int(now[1] + now[2] + now[3] + now[0])
        if not visited[value_l]:
            visited[value_l] = 1
            q.append([fill_zero(str(value_l)), record+"L"])

        # R
        value_r = int(now[3] + now[0] + now[1] + now[2])
        if not visited[value_r]:
            visited[value_r] = 1
            q.append([fill_zero(str(value_r)), record+"R"])

t = int(input())
for tc in range(1,t+1):
    s, g = map(str,input().split())
    s, g = fill_zero(s), fill_zero(g)
    bfs(s)

# Pass