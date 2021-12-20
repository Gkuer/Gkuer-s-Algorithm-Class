import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*10 for _ in range(1001)]

for i in range(10):
    arr[0][i] = 1

for i in range(1,1001):
    for x in range(10):
        arr[i][x] = sum(arr[i-1][x:])

print(sum(arr[n-1])%10007)

# Pass