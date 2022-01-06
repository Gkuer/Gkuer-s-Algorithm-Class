import sys
import heapq
input = sys.stdin.readline

n = int(input())
minus_q = []
plus_q = []
for i in range(n):
    data = int(input())
    if data < 0:
        heapq.heappush(minus_q,(-data,data))
    elif data > 0:
        heapq.heappush(plus_q,data)
    else:
        if minus_q and plus_q:
            minus_data, plus_data = heapq.heappop(minus_q)[0], heapq.heappop(plus_q)
            if minus_data < plus_data:
                print(-minus_data)
                heapq.heappush(plus_q,plus_data)
            elif minus_data > plus_data:
                print(plus_data)
                heapq.heappush(minus_q,(minus_data,-minus_data))
            else:
                print(-minus_data)
                heapq.heappush(plus_q,plus_data)
        elif minus_q or plus_q:
            if minus_q:
                print(heapq.heappop(minus_q)[1])
            else:
                print(heapq.heappop(plus_q))
        else:
            print(0)
# Pass