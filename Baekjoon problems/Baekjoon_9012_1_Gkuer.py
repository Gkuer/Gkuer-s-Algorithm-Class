import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    map = input().strip()
    stack = []
    for i in map:
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("NO")
                break
        else:
            stack.append(i)

    else:
        if stack:
            print("NO")
        else:
            print("YES")

# Pass