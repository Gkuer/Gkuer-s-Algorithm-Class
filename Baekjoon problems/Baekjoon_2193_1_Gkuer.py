import sys
input = sys.stdin.readline

n = int(input())
maps = [[0,0] for _ in range(91)]
maps[0] = [1,0]
maps[1] = [0,1]
maps[2] = [1,1]
for i in range(3,91):
    maps[i][0] = maps[i-1][1]
    maps[i][1] = sum(maps[i-1])

print(sum(maps[n-1]))

# Pass