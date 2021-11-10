import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def dfs(idx,idy):
    if temps[idx][idy]:
        return temps[idx][idy]

    for i in range(4):
        nr = idx + dirs[i][0]*int(maps[idx][idy])
        nc = idy + dirs[i][1]*int(maps[idx][idy])
        if 0 <= nr < n and 0 <= nc < m:
            if maps[nr][nc] != "H":
                if [nr,nc] not in visited:
                    visited.append([nr,nc])
                    temps[idx][idy] = max(temps[idx][idy], dfs(nr,nc)+1)
                    visited.pop()
                else:
                    return 987654321


    return temps[idx][idy]

n, m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
visited = []

temps = [[0] * m for _ in range(n)]
visited.append([0,0])
res = dfs(0,0)

if res >= 987654321:
    print(-1)
else:
    print(res+1)

# Pass