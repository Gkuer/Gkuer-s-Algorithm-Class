import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = []
maps.append([0]*(m+1))
for _ in range(n):
    maps.append([0] + list(map(int, list(input().strip()))))

mx = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if maps[i][j] == 1:
            res = min(maps[i-1][j], maps[i][j-1], maps[i-1][j-1]) + 1
            maps[i][j] = res
            if res > mx:
                mx = res

print(mx*mx)

# Pass