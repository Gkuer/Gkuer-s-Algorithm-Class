import sys
import heapq
import math
input = sys.stdin.readline
inf = math.inf

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    dp = [inf] * (n+1)
    dp[start] = 0

    while q:
        weight, pos = heapq.heappop(q)

        if weight > dp[pos]:
            continue

        for val, next_pos in maps[pos]:
            next_weight = val + weight
            if next_weight < dp[next_pos]:
                dp[next_pos] = next_weight
                heapq.heappush(q,[next_weight,next_pos])

    return dp

n, e = map(int,input().split())
maps = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int,input().split())
    maps[a].append([c,b])
    maps[b].append([c,a])

v1, v2 = map(int,input().split())

from_1 = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

ans = min(from_1[v1] + from_v1[v2] + from_v2[n], from_1[v2] + from_v2[v1] + from_v1[n])

print(ans if ans < inf else -1)

# Pass