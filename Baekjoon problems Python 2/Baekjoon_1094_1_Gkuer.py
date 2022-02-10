import sys
import heapq
input = sys.stdin.readline

x = int(input())
maps = [64]
sm = 64

while sm != x:
    mn = heapq.heappop(maps)
    mn_half = mn // 2

    if sm - mn_half >= x:
        heapq.heappush(maps,mn_half)
        sm -= mn_half
    else:
        heapq.heappush(maps, mn_half)
        heapq.heappush(maps, mn_half)

print(len(maps))

# Pass