import sys
input = sys.stdin.readline

def find(idx,idy,x):
    global res
    val = maps[idx][idy]
    flag = False
    for i in range(idx,idx+x):
        for j in range(idy,idy+x):
            if maps[i][j] != val:
                res += "("
                flag = True
                find(idx, idy, x//2)
                find(idx, idy + x // 2, x // 2)
                find(idx + x // 2, idy, x // 2)
                find(idx + x // 2, idy + x // 2, x // 2)
                res += ")"
                break
        if flag:
            break

    if not flag:
        res += str(val)

n = int(input())
maps = [list(map(int,input().strip())) for _ in range(n)]

res = ""
find(0,0,n)
print(res)

# Pass