import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    k = int(input())
    n = int(input())
    maps = [[i for i in range(1,n+1)]]
    for i in range(1,k+1):
        temps = []
        for x in range(n):
            cnt = 0
            for y in range(x+1):
                cnt += maps[-1][y]
            temps.append(cnt)
        maps.append(temps)

    print(maps[-1][-1])

# Pass