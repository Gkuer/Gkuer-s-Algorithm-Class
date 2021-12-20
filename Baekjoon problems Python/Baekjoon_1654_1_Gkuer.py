import sys
input = sys.stdin.readline

n, m = map(int,input().split())

maps = []
for i in range(n):
    maps.append(int(input()))

start = 1
end = max(maps)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += maps[i] // mid

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# Pass