import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    a = int(input())
    if a == 0:
        maps.pop()
    else:
        maps.append(a)

print(sum(maps))

# Pass