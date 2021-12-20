import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 301
for i in range(n):
    arr[i] = int(input())

maps = [0] * 301
maps[0] = arr[0]
maps[1] = arr[0]+arr[1]
maps[2] = max(arr[0]+arr[2], arr[1]+arr[2])
for i in range(3,n):
    maps[i] = max(maps[i-2]+arr[i], maps[i-3]+arr[i-1]+arr[i])

print(maps[n-1])

# Pass