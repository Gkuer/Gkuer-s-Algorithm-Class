import sys
input = sys.stdin.readline

def dfs(idx,idy):
    if idx == n-1 and idy == n-1:
        return 1

    if dp[idx][idy] == -1:
        dp[idx][idy] = 0
        x1, y1 = idx + maps[idx][idy], idy
        x2, y2 = idx, idy+maps[idx][idy]
        if 0 <= x1 < n and 0 <= y1 < n: dp[idx][idy] += dfs(x1,y1)
        if 0 <= x2 < n and 0 <= y2 < n: dp[idx][idy] += dfs(x2,y2)

    return dp[idx][idy]


n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]
print(dfs(0,0))

# Pass