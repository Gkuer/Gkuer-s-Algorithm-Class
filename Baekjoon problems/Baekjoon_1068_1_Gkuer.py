import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = list(map(int,input().split()))
s = int(input())
q = deque()
q.append(s)
maps[s] = -2
while q:
    now = q.popleft()
    for i in range(n):
        if maps[i] == now:
            q.append(i)
            maps[i] = -2

try:
    q.append(maps.index(-1))
    cnt = 0
    while q:
        now = q.pop()
        flag = False
        for i in range(n):
            if maps[i] == now:
                flag = True
                q.append(i)
        if not flag:
            cnt += 1
    print(cnt)
except:
    print(0)

# Pass