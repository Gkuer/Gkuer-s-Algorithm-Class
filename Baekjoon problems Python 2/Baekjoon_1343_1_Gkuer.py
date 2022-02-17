import sys
input = sys.stdin.readline

maps = input().strip()
maps = maps.replace("XXXX","AAAA")
maps = maps.replace("XX","BB")

for i in maps:
    if i == "X":
        print(-1)
        break
else:
    print(maps)

# Pass