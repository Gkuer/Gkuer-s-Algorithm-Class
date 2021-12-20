import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deck = deque()
for i in range(n):
    command = input().strip()
    if 'push' in command:
        command, val = command.split()

    if command == 'push_back':
        deck.append(val)
    elif command == 'push_front':
        deck.appendleft(val)
    elif command == 'pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(deck))
    elif command == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif command == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)
    else:
        print("error")

# Pass