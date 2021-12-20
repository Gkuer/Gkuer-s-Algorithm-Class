import sys
import math
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    maps = list(map(int,input().split()))
    dp = [[0]*n for _ in range(n)]

    for j in range(1,n):
        for i in range(j-1,-1,-1):
            dp[i][j] = math.inf
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j])
            dp[i][j] += sum(maps[i:j+1])

    print(dp[0][n-1])

# Pass