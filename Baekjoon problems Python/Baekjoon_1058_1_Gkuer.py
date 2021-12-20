import sys
input = sys.stdin.readline

def dfs(now,cnt,start):
    if cnt > 1:
        return

    for x in range(n):
        if maps[now][x] == "Y" and not visited[x] and x != start:
            visited[x] = 1
            dfs(x,cnt+1,start)

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))

ans = 0
for i in range(n):
    visited = [0]*n
    for x in range(n):
        if maps[i][x] == "Y" and x != i:
            if not visited[x]:
                visited[x] = 1
                dfs(x,1,i)

    ans = max(sum(visited), ans)

print(ans)

# Wrong Anser
