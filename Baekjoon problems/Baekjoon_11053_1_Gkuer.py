import sys

input = sys.stdin.readline

n = int(input())
maps = list(map(int, input().split()))
arr = [0] * 1001
if n == 1:
    print(1)
else:
    arr[0] = 1
    if maps[1] > maps[0]:
        arr[1] = 2
    else:
        arr[1] = 1

    for i in range(2, n):
        temps = []
        for x in range(i):
            if maps[x] < maps[i]:
                temps.append(arr[x])
        if temps:
            arr[i] = max(temps) + 1
        else:
            arr[i] = 1

    print(max(arr))

# Pass