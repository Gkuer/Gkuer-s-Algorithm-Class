import sys
import math
input = sys.stdin.readline
inf = math.inf

def dfs(pos,visited,memory):
    if memory >= m:
        return costs[pos]

    if dp[pos][visited] != inf:
        return dp[pos][visited]

    for i in range(n):
        if visited & (1<<i):
            continue
        dp[pos][visited] = min(dp[pos][visited], dfs(i,visited|(1<<i),memory+memories[i])+costs[pos])

    return dp[pos][visited]

n, m = map(int,input().split())
memories = list(map(int,input().split()))
costs = list(map(int,input().split()))
dp = [[inf]*(1<<n) for _ in range(n)]

ans = inf
for i in range(n):
    ans = min(ans,dfs(i,(1<<i),memories[i]))

print(ans)

# Fail: Overflow Error