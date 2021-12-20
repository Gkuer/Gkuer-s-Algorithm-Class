import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

for goal in range(1, k+1):
    temp = []
    for coin in coins:
        if coin <= goal and dp[goal-coin] != -1:
            temp.append(dp[goal-coin])

    if not temp:
        dp[goal] = -1
    else:
        dp[goal] = min(temp) + 1

print(dp[k])

# Pass