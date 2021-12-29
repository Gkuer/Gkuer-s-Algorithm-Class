import sys
import math
input = sys.stdin.readline

n = int(input())
inf = math.inf
dp = [0]*(n+1)
dp[0], dp[1] = 0, 1

for i in range(2,n+1):
    j = 1
    min_val = math.inf
    while j**2 <= i:
        min_val = min(min_val, dp[i-(j**2)])
        j += 1

    dp[i] = min_val+1

print(dp[n])

# Pass