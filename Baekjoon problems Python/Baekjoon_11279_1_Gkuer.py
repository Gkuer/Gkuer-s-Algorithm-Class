import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(q,(-x,x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
            
# Pass