import copy
import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

dp = [[] for _ in range(n)]
dp[0] = [maps[0]]

for i in range(1,n):
    for j in range(i):
        if maps[i] > maps[j] and len(dp[j]) > len(dp[i]):
            dp[i] = copy.deepcopy(dp[j])
    dp[i].append(maps[i])

dp.sort(key=lambda x: len(x))
print(len(dp[-1]))
print(*dp[-1])

# Pass