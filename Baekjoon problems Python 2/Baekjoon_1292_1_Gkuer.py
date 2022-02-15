import sys
input = sys.stdin.readline

n, m = map(int,input().split())

maps = []
cnt = 1
while len(maps) <= 1000:
    for _ in range(cnt):
        maps.append(cnt)
    cnt += 1

print(sum(maps[n-1:m]))

# Pass