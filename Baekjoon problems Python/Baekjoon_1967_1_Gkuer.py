import sys

input = sys.stdin.readline
from collections import deque

sys.setrecursionlimit(10 ** 6)


def dfs(start):
    q = deque()
    visited = [-1] * (n + 1)
    q.append([start, 0])
    while q:
        now, point = q.popleft()
        visited[now] = point
        for i in maps[now]:
            if visited[i[0]] == -1:
                q.append([i[0], point + i[1]])

    return visited.index(max(visited))


def dfs2(start):
    if credit[start] != -1:
        return credit[start]

    credit[start] = 0
    for i in maps[start]:
        if credit[i[0]] == -1:
            credit[start] = max(credit[start], dfs2(i[0]) + i[1])
    return credit[start]


n = int(input())
maps = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    maps[a].append([b, c])
    maps[b].append([a, c])

credit = [-1] * (n + 1)
print(dfs2(dfs(1)))

# Pass
