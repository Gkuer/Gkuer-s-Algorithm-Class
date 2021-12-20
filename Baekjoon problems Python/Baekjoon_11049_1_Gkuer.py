import sys
import math
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for j in range(1,n):
    for i in range(n-j):
        node = j+i
        dp[i][node] = math.inf
        for k in range(i,node):
            dp[i][node] = min(dp[i][node], dp[i][k] + dp[k+1][node] + maps[i][0]*maps[k][1]*maps[node][1])

print(dp[0][n-1])

# Pass