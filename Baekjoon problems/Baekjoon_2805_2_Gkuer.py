import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = list(map(int,input().split()))

s, e = 1, max(maps)

while s <= e:
    mid = (s + e) // 2

    temp = 0
    for i in maps:
        if i > mid:
            temp += i - mid

    if temp < m:
        e = mid-1
    else:
        s = mid+1

print(e)

# Pass