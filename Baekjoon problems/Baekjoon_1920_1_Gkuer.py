import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))
maps.sort()
m = int(input())
arr = list(map(int,input().split()))

for i in arr:
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end) // 2
        if maps[mid] == i:
            print(1)
            break
        elif maps[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0)

# Pass