import sys
input = sys.stdin.readline

def dfs(idx):
    if idx in visited:
        return

    if not maps[idx]:
        ans_list[idx] += 1
        return

    visited.append(idx)
    ans_list[idx] += 1

    for x in maps[idx]:
        dfs(x)

n, m = map(int,input().split())
ans_list = [0] + [0]*n
maps = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    maps[a].append(b)

for i in range(1,n+1):
    if maps[i]:
        for x in maps[i]:
            visited = []
            dfs(x)

mx = 0
for i in range(1,n+1):
    if ans_list[i] > mx:
        mx = ans_list[i]
        ans = [i]
    elif ans_list[i] == mx:
        ans.append(i)

print(*ans)

# Fail: TimeOver