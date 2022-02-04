import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [0] * (n+1)
stack = deque()
for _ in range(m):
    a, b = map(int,input().split())

    if maps[a]:
        temp = []
        while stack[-1] != a:
            c = stack.pop()
            temp.append(c)

        stack.append(b)
        maps[b] = 1

        while temp:
            c = temp.pop()
            stack.append(c)

    elif maps[b]:
        temp = []
        while stack[0] != b:
            c = stack.popleft()
            temp.append(c)

        stack.appendleft(a)
        maps[a] = 1

        while temp:
            c = temp.pop()
            stack.appendleft(c)
    else:
        stack.appendleft(a)
        stack.append(b)
        maps[a] = 1
        maps[b] = 1

for i in range(1,n+1):
    if not maps[i]:
        stack.append(i)

print(*stack)

# Fail : Time Over n