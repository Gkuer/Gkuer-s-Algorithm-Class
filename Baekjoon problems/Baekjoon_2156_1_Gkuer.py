import sys
input = sys.stdin.readline

n = int(input())
maps = [0]*10001
for i in range(n):
    maps[i] = int(input())
res = [0]*10001
res[0] = maps[0]
res[1] = maps[1] + maps[0]
res[2] = max(res[1],maps[0]+maps[2],maps[1]+maps[2])
if n >= 3:
    for i in range(3,n):
        res[i] = max(res[i-1],res[i-2]+maps[i],res[i-3]+maps[i-1]+maps[i])
print(res[n-1])

# Pass