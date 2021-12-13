import sys
input = sys.stdin.readline

one = "x" + input().strip()
two = "x" + input().strip()
dp = [["" for _ in range(len(two))] for _ in range(len(one))]

for i in range(1,len(one)):
    for j in range(1,len(two)):
        if one[i] == two[j]:
            dp[i][j] = dp[i-1][j-1] + one[i]
        else:
            if len(dp[i-1][j]) < len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

print(len(dp[len(one)-1][len(two)-1]))
print(dp[len(one)-1][len(two)-1])

# Pass