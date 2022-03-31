inf = 987654321
n = int(input())
maps = [inf for _ in range(n+1)]
temps = [0, inf, 1, inf, 2, 1]

if n >= 5:
    maps[1], maps[2], maps[3], maps[4], maps[5] = inf, 1, inf, 2, 1
else:
    for i in range(1,n+1):
        maps[i] = temps[i]

for i in range(6, n+1):
    maps[i] = min(maps[i-2],maps[i-5])+1

if maps[n] >= inf:
    print(-1)
else:
    print(maps[n])

# Pass