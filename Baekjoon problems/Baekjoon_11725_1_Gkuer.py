import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = []
for i in range(n-1):
    maps.append(list(map(int,input().split())))

start = 1
q = deque()
q.append(start)
temps = [0]*(n+1)
stack = []
while q:
    now = q.popleft()

    for i in range(n-1):
        if now in maps[i] and maps[i] not in stack:
            for x in maps[i]:
                if x != now:
                    temps[x] = now
                    q.append(x)
                    stack.append(maps[i])

for i in range(2,len(temps)):
    print(temps[i])

# Fail: Time over