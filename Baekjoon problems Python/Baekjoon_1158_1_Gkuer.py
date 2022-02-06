from collections import deque

n, k = map(int,input().split())
stack = deque([i for i in range(1,n+1)])

print("<", end="")

cnt = 1
while stack:
    a = stack.popleft()

    if cnt % k == 0:
        if stack:
            print(a,end=", ")
        else:
            print(a,end="")
    else:
        stack.append(a)
    cnt += 1

print(">")

# Pass