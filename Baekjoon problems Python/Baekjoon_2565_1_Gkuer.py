import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
maps.sort()
dp = [0] * n
for i in range(n):
    for j in range(i):
        if maps[j][1] < maps[i][1] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))

# Pass