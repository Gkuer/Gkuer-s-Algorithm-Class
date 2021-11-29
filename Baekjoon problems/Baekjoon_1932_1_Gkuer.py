import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dp = [[0]*i for i in range(1,n+1)]
dp[0][0] = maps[0][0]
for i in range(n-1):
    for x in range(len(maps[i])):
        dp[i+1][x] = max(dp[i+1][x], maps[i+1][x]+dp[i][x])
        dp[i+1][x+1] = max(dp[i+1][x+1],maps[i+1][x+1]+dp[i][x])

print(max(dp[n-1]))

# Pass