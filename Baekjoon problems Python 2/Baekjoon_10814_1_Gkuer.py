n = int(input())
maps = []
for i in range(n):
    old, name = input().split()
    maps.append([int(old),i,name])

for i,j,k in sorted(maps):
    print(str(i) + " " + k)