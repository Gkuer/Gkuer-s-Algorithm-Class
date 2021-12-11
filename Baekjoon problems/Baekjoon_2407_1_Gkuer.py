import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dp = [0] * 101
dp[0] = 1
for i in range(1,101):
    dp[i] = dp[i-1]*i

print(dp[n]//(dp[m]*dp[n-m]))

# Pass