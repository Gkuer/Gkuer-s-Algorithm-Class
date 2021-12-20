import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*23
arr[1] = 0
arr[2] = 1

for i in range(3,n+2):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n+1])

# Pass