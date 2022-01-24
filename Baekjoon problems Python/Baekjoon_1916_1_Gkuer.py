import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dp[start] = 0

    while q:
        weight, now = heapq.heappop(q)

        if weight > dp[now]:
            continue

        for next_weight,next_pos in maps[now]:
            res_weight = next_weight + weight
            if res_weight < dp[next_pos]:
                dp[next_pos] = res_weight
                heapq.heappush(q,(res_weight,next_pos))


n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]
dp = [inf]*(n+1)

for _ in range(m):
    s, g, w = map(int,input().split())
    maps[s].append((w,g))

f, e = map(int,input().split())

dijkstra(f)
print(dp[e])

# Pass
