import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
def dfs(idx, idy):
    if temps[idx][idy] != -1:
        return temps[idx][idy]

    temps[idx][idy] = 0
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < n:
            if maps[nr][nc] < maps[idx][idy]:
                temps[idx][idy] = max(temps[idx][idy],dfs(nr,nc)+1)

    return temps[idx][idy]

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
temps = [[-1]*n for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
ans = 0
for i in range(n):
    for x in range(n):
        ans = max(ans,dfs(i,x))
print(ans+1)
# Pass 