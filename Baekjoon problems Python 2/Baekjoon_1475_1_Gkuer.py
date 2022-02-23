import sys
input = sys.stdin.readline

n = input().strip()
maps = [0 for _ in range(10)]

for i in n:
    if i != "6" and i != "9":
        maps[int(i)] += 1
    else:
        if maps[6] < maps[9]:
            maps[6] += 1
        else:
            maps[9] += 1

print(max(maps))

# Pass