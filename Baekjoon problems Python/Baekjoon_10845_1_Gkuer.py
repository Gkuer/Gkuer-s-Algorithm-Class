import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    command = input().strip()
    if 'push' in command:
        command, val = command.split()
    if command == "push":
        q.append(int(val))
    elif command == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
# Pass