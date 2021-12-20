import sys
input = sys.stdin.readline

t = int(input())
arr = [0] * 101
arr[0] = 1
arr[1] = 1
arr[2] = 1
for i in range(3,101):
    arr[i] = arr[i-3] + arr[i-2]

for tc in range(1, t+1):
    n = int(input())
    print(arr[n-1])

# Pass
