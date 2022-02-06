n, m = map(int,input().split())
maps = [0]
t = 1
while len(maps) <= 1000:
    for i in range(1,t+1):
        maps.append(t)
    t += 1

print(sum(maps[n:m+1]))

# Pass