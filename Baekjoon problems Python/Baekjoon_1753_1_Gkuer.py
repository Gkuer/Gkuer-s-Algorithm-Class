import sys
import heapq

def dijkstra(start):
    q = []
    dp[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        wei, now = heapq.heappop(q)
        if wei > dp[now]:
            continue

        for weight, nextto in maps[now]:
            nextval = weight + wei
            if dp[nextto] > nextval:
                dp[nextto] = nextval
                heapq.heappush(q,(nextval, nextto))


input = sys.stdin.readline

v, e = map(int,input().split())
inf = sys.maxsize
k = int(input())
maps = [[] for _ in range(v+1)]
dp = [inf] * (v+1)

for i in range(e):
    u, to, w = map(int,input().split())
    maps[u].append((w,to))

dijkstra(k)

for i in dp[1:]:
    if i == inf:
        print("INF")
    else:
        print(i)

# Pass