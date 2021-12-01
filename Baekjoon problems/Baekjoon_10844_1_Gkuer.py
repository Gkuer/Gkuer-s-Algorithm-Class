import sys
input = sys.stdin.readline

n = int(input())
maps = [[0 for _ in range(10)] for _ in range(101)]
for i in range(1,10):
    maps[0][i] = 1

for i in range(1,101):
    for j in range(10):
        if j == 0:
            maps[i][j] = maps[i-1][1]
        elif j == 9:
            maps[i][j] = maps[i-1][8]
        else:
            maps[i][j] = maps[i-1][j-1] + maps[i-1][j+1]

print(sum(maps[n-1])%1000000000)

# Pass