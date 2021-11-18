import sys
input = sys.stdin.readline

t = int(input())
arr = [[] for _ in range(41)]
arr[0] = [1,0]
arr[1] = [0,1]

def fibonacci(x):
    if arr[x]:
        return arr[x]

    a, b = fibonacci(x-1), fibonacci(x-2)
    arr[x] = [a[0] + b[0], a[1] + b[1]]
    return arr[x]

for _ in range(t):
    n = int(input())
    print(*fibonacci(n))

# Pass