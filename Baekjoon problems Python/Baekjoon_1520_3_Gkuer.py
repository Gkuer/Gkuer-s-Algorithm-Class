import sys
input = sys.stdin.readline

def dfs(idx,idy):
    if idx == n-1 and idy == m-1:
        return 1

    if temps[idx][idy] != -1:
        return temps[idx][idy]

    temps[idx][idy] = 0
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if maps[nr][nc] < maps[idx][idy]:
                temps[idx][idy] += dfs(nr,nc)

    return temps[idx][idy]

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
temps = [[-1]*m for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
print(dfs(0,0))

# Pass