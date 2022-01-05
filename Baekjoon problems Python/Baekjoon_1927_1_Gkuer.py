import sys
input = sys.stdin.readline
import heapq

n = int(input())
maps = []
for _ in range(n):
    query = int(input())
    if query:
        heapq.heappush(maps,query)
    else:
        if maps:
            print(heapq.heappop(maps))
        else:
            print(0)

# Pass