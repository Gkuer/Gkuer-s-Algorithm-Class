import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    command = input().strip()
    if 'push' in command:
        command, val = command.split()
    if command == "push":
        stack.append(int(val))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)

# Pass