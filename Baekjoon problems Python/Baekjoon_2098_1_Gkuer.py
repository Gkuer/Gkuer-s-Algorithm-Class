import sys
import math
input = sys.stdin.readline

def dfs(pos,visited):
    if visited == (1<<n)-1:
        if maps[pos][0]:
            return maps[pos][0]
        else:
            return inf

    if dp[pos][visited] != inf:
        return dp[pos][visited]

    for next in range(1,n):
        if not maps[pos][next]:
            continue
        if visited & (1<<next):
            continue
        dp[pos][visited] = min(dp[pos][visited], dfs(next,visited|(1<<next))+maps[pos][next])

    return dp[pos][visited]

n = int(input())
inf = math.inf
dp = [[inf]*(1<<n) for _ in range(n)]

maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

print(dfs(0,1))

# Pass