import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

dpp = [0 for _ in range(n)]
dpm = [0 for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if maps[i] > maps[j] and dpp[i] < dpp[j]:
            dpp[i] = dpp[j]
    dpp[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if maps[i] > maps[j] and dpm[i] < dpm[j]:
            dpm[i] = dpm[j]
    dpm[i] += 1

for i in range(n):
    ans[i] += dpp[i] + dpm[i] - 1

print(max(ans))

# Pass
