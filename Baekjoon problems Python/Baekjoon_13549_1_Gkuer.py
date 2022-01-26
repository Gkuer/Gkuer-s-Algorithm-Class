import sys
import heapq
input = sys.stdin.readline

def bfs(start):
    q = []
    heapq.heappush(q,[0,start])
    maps[start] = True
    while q:
        cnt, pos = heapq.heappop(q)

        if pos == k:
            print(cnt)
            return

        for next in [pos + 1, pos - 1, pos * 2]:
            if 0 <= next <= 100000:
                if not maps[next]:
                    if next == pos * 2:
                        maps[next] = True
                        heapq.heappush(q, [cnt,next])
                    else:
                        maps[next] = True
                        heapq.heappush(q,[cnt+1,next])

n, k = map(int,input().split())
maps = [False] * 100001

bfs(n)

# Pass