import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 1001
arr[0] = 1
arr[1] = 3
for i in range(2,1001):
    arr[i] = arr[i-1] + arr[i-2] * 2

print(arr[n-1]%10007)

# Pass