import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    a, b = input().split()
    maps.append([int(a),b,i])

maps.sort(key=lambda x: (x[0],x[2]))

for i,j,k in maps:
    print(i,j,)

# Pass