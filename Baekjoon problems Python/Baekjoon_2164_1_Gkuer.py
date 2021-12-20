import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [i for i in range(1,n+1)]
q = deque(maps)
while len(q) >= 2:
    a = q.popleft()
    b = q.popleft()
    q.append(b)

print(q[0])

# Pass