import sys
input = sys.stdin.readline

def dfs(idx,idy,flag,start, cnt):
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if [nr,nc] == start and cnt >= 3:
                return True
            elif visited[nr][nc] == 0 and maps[nr][nc] == flag:
                visited[nr][nc] = 1
                res = dfs(nr,nc,flag,start,cnt+1)
                if res:
                    return True
                else:
                    visited[nr][nc] = 0
    return False

n, m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

check = False
for i in range(n):
    for x in range(m):
        visited = [[0]*m for _ in range(n)]
        visited[i][x] = 1
        if dfs(i,x,maps[i][x],[i,x],0):
            print("Yes")
            check = True
            break
    if check:
        break
else:
    print("No")

# Pass