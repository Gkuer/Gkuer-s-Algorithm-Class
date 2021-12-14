import sys
input = sys.stdin.readline

n = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
max_tp = [0] * 3
min_tp = [0] * 3

for i in range(n):
    a, b, c = map(int,input().split())
    for j in range(3):
        if j == 0:
            max_tp[j] = max(max_dp[0], max_dp[1]) + a
            min_tp[j] = min(min_dp[0], min_dp[1]) + a
        elif j == 2:
            max_tp[j] = max(max_dp[1], max_dp[2]) + c
            min_tp[j] = min(min_dp[1], min_dp[2]) + c
        else:
            max_tp[j] = max(max_dp[0], max_dp[1], max_dp[2]) + b
            min_tp[j] = min(min_dp[0], min_dp[1], min_dp[2]) + b

    for j in range(3):
        max_dp[j] = max_tp[j]
        min_dp[j] = min_tp[j]

print(max(max_dp),min(min_dp))

# Pass