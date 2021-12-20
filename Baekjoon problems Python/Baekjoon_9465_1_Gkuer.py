import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(2)]
    arr = [[0 for _ in range(n)] for _ in range(2)]

    if n == 1:
        print(max(maps[0][0],maps[1][0]))
    else:
        arr[0][0], arr[1][0] = maps[0][0], maps[1][0]
        arr[0][1], arr[1][1] = maps[0][1]+arr[1][0], maps[1][1]+arr[0][0]

        for i in range(2,n):
            for x in range(2):
                arr[x][i] = max(arr[1-x][i-1]+maps[x][i], arr[x][i], arr[1][i-2]+maps[x][i], arr[0][i-2]+maps[x][i])

        print(max(arr[0][n-1],arr[1][n-1]))

# Pass