import sys
input = sys.stdin.readline

def factorial(x):
    if x <= 1:
        return 1

    return x * factorial(x-1)

t = int(input())
for tc in range(t):
    n, m = map(int,input().split())

    res = factorial(m) // (factorial(m-n) * factorial(n))

    print(int(res))

# Pass