import sys
input = sys.stdin.readline

def dfs(now):
    cycle.append(now)
    visited[now] = 1
    node = maps[now]
    if visited[node]:
        if node in cycle:
            subres = cycle[cycle.index(node):]
            return [len(subres), subres]

        return [0,[]]

    return dfs(node)

n = int(input())
maps = [0] + [0]*n
for i in range(1,n+1):
    maps[i] = int(input())

visited = [0] * (n + 1)
ans = 0
ans_list = []
for i in range(1,n+1):
    if not visited[i]:
        cycle = []
        a, res = dfs(i)
        if a > 0:
            ans += a
            ans_list += res

for i in range(1,n+1):
    if i == maps[i] and i not in ans_list:
        ans_list.append(i)
        ans += 1

print(ans)
for i in sorted(ans_list):
    print(i)

# Pass