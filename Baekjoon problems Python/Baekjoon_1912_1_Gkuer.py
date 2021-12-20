import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))
arr = [0]*n
arr[0] = maps[0]
for i in range(1,n):
    arr[i] = max(maps[i],arr[i-1]+maps[i])
print(max(arr))

# Pass