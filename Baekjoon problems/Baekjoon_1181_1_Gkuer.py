n = int(input())
maps = set()
for i in range(n):
    maps.add(input())
maps = list(maps)
maps = sorted(maps)
maps.sort(key=lambda x: len(x))
for map in maps:
    print(map)

# Pass