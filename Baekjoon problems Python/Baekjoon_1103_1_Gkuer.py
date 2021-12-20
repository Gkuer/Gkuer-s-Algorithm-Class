import sys
input = sys.stdin.readline

def dfs(idx,idy, cnt):
    global ans
    if ans == 987654:
        return

    for i in range(4):
        nr = idx + dirs[i][0]*int(maps[idx][idy])
        nc = idy + dirs[i][1]*int(maps[idx][idy])
        if 0 <= nr < n and 0 <= nc < m:
            if not visited[nr][nc] and maps[nr][nc] != "H":
                visited[nr][nc] = 1
                ans = max(ans, cnt+1)
                dfs(nr,nc,cnt+1)
                visited[nr][nc] = 0

            elif maps[nr][nc] == "H":
                ans = max(ans, cnt+1)
                continue

            else:
                ans = 987654
                return
        else:
            ans = max(ans,cnt+1)

n, m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
visited = [[0]*m for _ in range(n)]

ans = 0
dfs(0,0,0)
print(ans) if ans != 987654 else print(-1)

# Fail: Time Over