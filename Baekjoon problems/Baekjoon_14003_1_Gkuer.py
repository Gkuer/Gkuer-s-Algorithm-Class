import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))
dp = [[0,[]] for _ in range(n)]
dp[0] = [1,[maps[0]]]
for i in range(1,n):
    for j in range(i):
        if maps[i] > maps[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
            dp[i][1] = dp[j][1]

    dp[i][0] += 1
    dp[i][1] = dp[i][1] + [maps[i]]

dp.sort()
print(dp[-1][0])
print(*dp[-1][1])

# Fail: Time Over