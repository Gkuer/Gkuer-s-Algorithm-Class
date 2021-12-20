import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(x):
    if dp[x] != -1:
        return dp[x]

    res = []
    for i in rules[x]:
        res.append(solve(i))

    if not res:
        dp[x] = times[x]
        return times[x]
    else:
        dp[x] = max(res) + times[x]
        return max(res) + times[x]

t = int(input())
for tc in range(1,t+1):
    n, k = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    rules = [[] for _ in range(n+1)]
    for _ in range(k):
        s, g = map(int,input().split())
        rules[g].append(s)
    goal = int(input())
    dp = [-1] * (n+1)
    print(solve(goal))

# Pass