import sys
input = sys.stdin.readline

def cal(map1,map2):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += map1[i][k] * map2[k][j]

    for i in range(2):
        for j in range(2):
            res[i][j] %= 1000000007

    return res

n = int(input())

base = [[1,1],[1,0]]
ans = [[1,0],[0,1]]
n = bin(n)[2:]

for i in range(len(n)):
    pos = len(n)-1-i
    if n[pos] == '1':
        temp = base[:]
        while i > 0:
            temp = cal(temp,temp)
            i -= 1
        ans = cal(ans,temp)

print(ans[1][0]%1000000007)

# Pass