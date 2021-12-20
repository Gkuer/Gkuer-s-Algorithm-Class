import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()
    if a == ".":
        break

    else:
        a = a[:a.index(".")]

    stack = []
    for i in a:
        if i in ["[","]","(",")"]:
            if i == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    print("no")
                    break

            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    print("no")
                    break

            else:
                stack.append(i)
    else:
        if stack:
            print("no")
        else:
            print("yes")

# Pass