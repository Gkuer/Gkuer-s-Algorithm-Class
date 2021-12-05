import sys
input = sys.stdin.readline

n = int(input())
maps = [0] + list(map(int,input().split()))
arr = [0] * (n+1)
arr[1] = maps[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        if arr[i] < arr[i-j] + maps[j]:
            arr[i] = arr[i-j] + maps[j]
print(arr[n])

# Pass