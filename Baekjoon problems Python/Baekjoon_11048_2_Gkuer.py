import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = []
maps.append([0]*(m+1))
for i in range(n):
    maps.append([0] + list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        maps[i][j] = maps[i][j] + max(maps[i-1][j], maps[i][j-1], maps[i-1][j-1])

print(maps[n][m])

# Pass