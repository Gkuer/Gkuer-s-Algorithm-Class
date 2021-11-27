import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))

for i in range(1,n):
    maps[i][0] = min(maps[i-1][1], maps[i-1][2]) + maps[i][0]
    maps[i][1] = min(maps[i-1][0], maps[i-1][2]) + maps[i][1]
    maps[i][2] = min(maps[i-1][0], maps[i-1][1]) + maps[i][2]

print(min(maps[n-1][0], maps[n-1][1], maps[n-1][2]))
# Pass