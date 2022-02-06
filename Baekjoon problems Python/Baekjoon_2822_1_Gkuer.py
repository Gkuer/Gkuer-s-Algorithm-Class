maps = []
for i in range(8):
    maps.append([int(input()), i+1])

maps.sort(reverse=True)

sm = 0
for i in range(5):
    sm += maps[i][0]

print(sm)

ans = []
for i in range(5):
    ans.append(maps[i][1])

print(*sorted(ans))

# Pass