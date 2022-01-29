import sys
import math
import heapq
inf = math.inf
input = sys.stdin.readline

def dijkstra(start):
    dp = [inf] * (n+1)
    q = []
    heapq.heappush(q,[0,start])
    dp[start] = 0

    while q:
        weight, pos = heapq.heappop(q)

        if dp[pos] < weight:
            continue

        for val, next_pos in maps[pos]:
            next_weight = val + weight
            if next_weight < dp[next_pos]:
                dp[next_pos] = next_weight
                heapq.heappush(q,[next_weight, next_pos])

    for i in range(1,n+1):
        if dp[i] == inf:
            dp[i] = 0

    return dp[1:]

n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    maps[a].append((c,b))

for i in range(1,n+1):
    res = dijkstra(i)
    print(*res)

# Pass