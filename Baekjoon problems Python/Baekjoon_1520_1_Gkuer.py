import sys
input = sys.stdin.readline

def dfs(idx, idy):
    global cnt

    if idx == n-1 and idy == m-1:
        cnt += 1
        return

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and maps[nr][nc] < maps[idx][idy]:
                visited[nr][nc] = 1
                dfs(nr,nc)
                visited[nr][nc] = 0
    return

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[False]*m for _ in range(n)]
visited[0][0] = 1
cnt = 0
dfs(0,0)
print(cnt)

# Fail: Time Over