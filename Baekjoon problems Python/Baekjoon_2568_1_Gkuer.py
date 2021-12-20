from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    a, b = map(int,input().split())
    dp.append([a,b])

dp.sort()

orders = []
new_dp = []

for i in range(n):
    if not orders or orders[-1] < dp[i][1]:
        orders.append(dp[i][1])
        new_dp.append([len(orders)-1,dp[i][1]])
    else:
        orders[bisect_left(orders,dp[i][1])] = dp[i][1]
        new_dp.append([bisect_left(orders,dp[i][1]),dp[i][1]])


cnt = len(orders)-1
ans = []
for i in range(len(new_dp)-1,-1,-1):
    if cnt == new_dp[i][0]:
        ans.append(new_dp[i][1])
        cnt -= 1

print(n-len(ans))
for i in dp:
    if i[1] not in ans:
        print(i[0])

# Pass