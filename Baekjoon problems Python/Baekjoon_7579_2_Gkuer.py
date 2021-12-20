import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [0] + list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))
dp = [[0]*(sum(costs)+1) for _ in range(n+1)]

ans = sum(costs)
for i in range(1, n+1):
    for j in range(1, sum(costs)+1):
        if j < costs[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i]] + maps[i])

        if dp[i][j] >= m:
            ans = min(ans,j)

print(ans)

# Pass