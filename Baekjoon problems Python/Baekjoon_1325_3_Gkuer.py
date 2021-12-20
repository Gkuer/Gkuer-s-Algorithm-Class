import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
maps = [[] for _ in range(n + 1)]
temps = [-1] * (n + 1)

def dfs(now):
    if temps[now] != -1:
        return temps[now]

    temps[now] = 1
    for i in maps[now]:
        temps[now] += dfs(i)

    return temps[now]

for i in range(m):
    a, b = map(int, input().split())
    maps[b].append(a)

mx = -5
for i in range(1,n+1):
    if maps[i]:
        a = dfs(i)

        if mx < a:
            mx = a
            ans_list = [i]
        elif mx == a:
            ans_list.append(i)

print(*ans_list)

# Fail: Time Over