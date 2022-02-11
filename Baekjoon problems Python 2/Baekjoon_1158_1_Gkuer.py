import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
maps = deque([i for i in range(1,n+1)])

cnt = 0
print("<", end="")
while maps:
    cnt += 1
    a = maps.popleft()

    if cnt % k == 0:
        if len(maps) == 0:
            print(str(a), end="")
        else:
            print(str(a), end=", ")
    else:
        maps.append(a)

print(">")

# Pass