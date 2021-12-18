import sys
input = sys.stdin.readline

def dfs(info, length, last):
    if length == n:
        if info == (1<<10)-1:
            return 1
        else:
            return 0

    if dp[info][length][last] != -1:
        return dp[info][length][last]

    dp[info][length][last] = 0
    if last == 0:
        dp[info][length][last] += dfs(info|(1<<(last+1)),length+1,last+1)
    elif last == 9:
        dp[info][length][last] += dfs(info|1<<(last-1),length+1,last-1)
    else:
        dp[info][length][last] += dfs(info|1<<(last+1),length+1,last+1)
        dp[info][length][last] += dfs(info|1<<(last-1),length+1,last-1)

    dp[info][length][last] %= 1000000000
    return dp[info][length][last]

n = int(input())
dp = [[[-1]*10 for _ in range(101)] for _ in range((1<<10))]

ans = 0
for i in range(1,10):
    ans += dfs((1<<i), 1, i) # info, length, last
    ans %= 1000000000

print(ans)

# Pass