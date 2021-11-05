import sys
input = sys.stdin.readline

def dfs(idx, idy, per, cnt):
    if cnt == n:
        ans.append(per)
        return

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < 2*n+1 and 0 <= nc < 2*n+1:
            if direction[i] and not maps[nr][nc]:
                maps[nr][nc] = 1
                dfs(nr,nc,per * direction[i], cnt+1)
                maps[nr][nc] = 0

n, east, west, south, north = map(int,input().split())
east, west, south, north = east*0.01, west*0.01, south*0.01, north*0.01
direction = [east,west,south,north]
maps = [[0] * (2*n+1) for _ in range(2*n+1)]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
start_idx, start_idy = n, n

ans = []
maps[start_idx][start_idy] = 1
dfs(start_idx,start_idy, 1, 0)
print(sum(ans))
# Pass