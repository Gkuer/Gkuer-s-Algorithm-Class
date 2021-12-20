import sys
input = sys.stdin.readline

def dfs(idx, idy, cnt):
    global ans

    if ans < cnt:
        ans = cnt

    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < r and 0 <= nc < c:
            if not visited[nr][nc] and not already[maps[nr][nc]]:
                visited[nr][nc] = 1
                already[maps[nr][nc]] = 1
                dfs(nr, nc, cnt+1)
                visited[nr][nc] = 0
                already[maps[nr][nc]] = 0

r, c = map(int,input().split())
maps = [list(map(lambda x: ord(x)-65, input())) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
already = [0]*27
already[maps[0][0]] = 1
visited[0][0] = 1
dirs = [(0,1),(1,0),(-1,0),(0,-1)]
ans = 0


dfs(0,0,1)

print(ans)
# Pass