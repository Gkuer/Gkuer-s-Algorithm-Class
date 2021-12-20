import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(now,check):
    if now == 0:
        return 2

    if now == check:
        return 1
    elif (now + check) % 2:
        return 3
    else:
        return 4

def dfs(length,left,right):
    if length >= len(maps)-1:
        return 0

    if dp[length][left][right] != -1:
        return dp[length][left][right]

    dp[length][left][right] = min(dfs(length+1,maps[length],right)+check(left,maps[length]), dfs(length+1,left,maps[length])+check(right,maps[length]))

    return dp[length][left][right]

maps = list(map(int,input().split()))
dp = [[[-1]*5 for _ in range(5)] for _ in range(100000)]
print(dfs(0,0,0)) # length, left, right

# Pass