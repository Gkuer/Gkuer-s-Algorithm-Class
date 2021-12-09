n = int(input())

arr = [i**2 for i in range(1,317)]
dp = [0]*(n+1)
for i in range(1,n+1):
    temps = []
    for j in arr:
        if i - j < 0:
            break
        temps.append(dp[i-j])
    dp[i] = min(temps) + 1

print(dp[n])

# Pass