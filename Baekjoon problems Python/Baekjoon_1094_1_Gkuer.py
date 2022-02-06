n = int(input())
maps = [64]
t = 1
while sum(maps) > n:
    mn = min(maps)
    if sum(maps) - mn//2 >= n:
        maps[maps.index(mn)] = mn//2
    else:
        maps[maps.index(mn)] = mn//2
        maps.append(mn//2)
        t += 1

print(t)

# Pass