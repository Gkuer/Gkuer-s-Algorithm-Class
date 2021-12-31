import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = maps[1]
for i in range(2,n+1):
    dp[i] = dp[i-1] + maps[i]

for _ in range(m):
    s, e = map(int,input().split())
    print(dp[e] - dp[s-1])

# Pass