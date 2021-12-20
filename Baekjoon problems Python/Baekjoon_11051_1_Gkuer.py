import sys
input = sys.stdin.readline

n, k = map(int,input().split())
dp = [i for i in range(n+1)]
dp[0] = 1

for i in range(1,n+1):
    dp[i] *= dp[i-1]

print(dp[n]//(dp[k]*dp[n-k]) % 10007)

# Pass