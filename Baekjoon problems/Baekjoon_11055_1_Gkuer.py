import sys
input = sys.stdin.readline

n = int(input())
maps = [0] + list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i):
        if maps[i] > maps[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += maps[i]

print(max(dp))

# Pass