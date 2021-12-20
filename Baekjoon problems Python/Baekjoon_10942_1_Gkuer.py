import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))
dp = [[0] * n for _ in range(n)]

for j in range(n):
    for i in range(n-j):
        start = i
        end = i + j
        if start == end:
            dp[start][end] = 1
        elif maps[start] == maps[end]:
            if start+1 == end:
                dp[start][end] = 1
            elif dp[start+1][end-1]:
                dp[start][end] = 1

for i in range(int(input())):
    a, b = map(int,input().split())
    print(dp[a-1][b-1])

# Pass