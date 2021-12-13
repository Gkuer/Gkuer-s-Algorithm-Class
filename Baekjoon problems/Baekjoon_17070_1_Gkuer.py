import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)] # 0: 가로, 1: 세로, 2: 대각선
dp[0][1] = [1,0,0]

for i in range(n):
    for j in range(n):
        if j == 0:
            continue

        if not maps[i][j]:
            dp[i][j][0] += dp[i][j-1][0]
            dp[i][j][0] += dp[i][j-1][2]
            dp[i][j][1] += dp[i-1][j][1]
            dp[i][j][1] += dp[i-1][j][2]
            if not (maps[i-1][j]) and not(maps[i][j-1]):
                dp[i][j][2] += dp[i-1][j-1][0]
                dp[i][j][2] += dp[i-1][j-1][1]
                dp[i][j][2] += dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))

# Pass