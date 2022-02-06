n = int(input())
maps = {}
for i in range(n):
    a, b = input().strip().split()
    if b == "enter":
        maps[a] = 1
    else:
        del maps[a]

maps = sorted(maps.keys(), reverse=True)

for i in maps:
    print(i)

# Pass