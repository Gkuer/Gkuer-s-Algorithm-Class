import sys
from collections import deque

input = sys.stdin.readline

s, g = map(int,input().split())
q = deque()
q.append([s,0])
temps = [0] * 100001

while q:
    idx, time = q.popleft()

    if idx == g:
        break

    if idx > 100000 or idx < 0:
        continue

    if temps[idx] == 1:
        continue

    temps[idx] = 1

    if idx < g:
        q.append([idx+1,time+1])
        q.append([idx*2,time+1])
        q.append([idx-1,time+1])

    else:
        q.append([idx-1,time+1])

print(time)

# Pass