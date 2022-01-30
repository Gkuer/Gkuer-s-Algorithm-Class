import sys
import heapq
import math
inf = math.inf
input = sys.stdin.readline

def dijkstra(start):
    dp = [[inf,[]] for _ in range(n+1)]
    q = []
    heapq.heappush(q,[0,start,[start]])
    dp[start][0] = 0

    while q:
        weight, pos, record = heapq.heappop(q)

        if dp[pos][0] < weight:
            continue

        for val, next_pos in maps[pos]:
            next_weight = val + weight
            if next_weight < dp[next_pos][0]:
                dp[next_pos][0] = next_weight
                dp[next_pos][1] = record + [next_pos]
                heapq.heappush(q,[next_weight,next_pos,record+[next_pos]])

    return dp

n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    maps[a].append((c,b))

s, g = map(int,input().split())
res = dijkstra(s)

print(res[g][0])
print(len(res[g][1]))
print(*res[g][1])

# Pass