import sys
input = sys.stdin.readline

t = int(input())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

def dp(x):
    if arr[x]:
        return arr[x]

    arr[x] = dp(x - 1) + dp(x - 2) + dp(x - 3)
    return arr[x]

for tc in range(t):
    n = int(input())
    print(dp(n))

# Pass