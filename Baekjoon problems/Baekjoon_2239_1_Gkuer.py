import sys
input = sys.stdin.readline

def cal(x,y):
    res = (x//3)*3 + y//3
    return res

def dfs(n):
    if n == 81:
        for i in maps:
            print("".join(map(str,i)))
        return True

    x, y= n//9, n%9

    if maps[x][y]:
        return dfs(n+1)

    for i in range(1,10):
        if not rows[x][i] and not cols[y][i] and not sqrs[cal(x,y)][i]:
            rows[x][i] = cols[y][i] = sqrs[cal(x,y)][i] = 1
            maps[x][y] = i
            if dfs(n+1):
                return True
            rows[x][i] = cols[y][i] = sqrs[cal(x, y)][i] = 0
            maps[x][y] = 0
    return False

maps = [list(map(int,input().strip())) for _ in range(9)]
rows = [[0]*10 for _ in range(9)]
cols = [[0]*10 for _ in range(9)]
sqrs = [[0]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if maps[i][j]:
            rows[i][maps[i][j]] = cols[j][maps[i][j]] = sqrs[cal(i,j)][maps[i][j]] = 1

dfs(0)

# Pass