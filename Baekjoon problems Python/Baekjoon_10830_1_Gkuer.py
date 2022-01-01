import sys
input = sys.stdin.readline

def mul(map1,map2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += (map1[i][k] * map2[k][j])

    for i in range(n):
        for j in range(n):
            res[i][j] %= 1000

    return res

n, b = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

b = bin(b)[2:]

ans = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            ans[i][j] = 1

for i in range(len(b)):
    pos = len(b) - i - 1
    if b[pos] == '1':
        temp = maps[:]
        while i > 0:
            temp = mul(temp,temp)
            i -= 1
        ans = mul(ans,temp)

for i in range(n):
    print(*ans[i])

# Pass