import sys
input = sys.stdin.readline

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

maps = input().strip()

for i in cro:
    maps = maps.replace(i,"1")

print(len(maps))

# Pass