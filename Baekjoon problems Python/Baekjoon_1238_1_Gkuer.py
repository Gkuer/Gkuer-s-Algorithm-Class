import sys
import math
import heapq
inf = math.inf
input = sys.stdin.readline

def dijkstra(start):
    q = []
    dp = [inf] * (n+1)
    dp[start] = 0
    heapq.heappush(q,[0,start])

    while q:
        weight, pos = heapq.heappop(q)

        if weight > dp[pos]:
            continue

        for val, next_pos in maps[pos]:
            next_weight = val + weight
            if next_weight < dp[next_pos]:
                dp[next_pos] = next_weight
                heapq.heappush(q, [next_weight,next_pos])

    return dp

n, m, x = map(int,input().split())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    maps[a].append([c,b])

coming = dijkstra(x)
ans = [0]
for i in range(1,n+1):
    res = dijkstra(i)
    ans.append(coming[i] + res[x])

print(max(ans))

# Pass