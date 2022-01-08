import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_q = []
    max_q = []
    cnt = 0
    visit = [False] * 1000000
    for num in range(k):
        oper, val = input().split()
        if oper == 'I':
            cnt += 1
            heapq.heappush(min_q,[int(val),num])
            heapq.heappush(max_q,[-int(val),num])
            visit[num] = True
        else:
            if val == "1":
                while max_q and not visit[max_q[0][1]]:
                    heapq.heappop(max_q)

                if max_q:
                    visit[max_q[0][1]] = False
                    heapq.heappop(max_q)
            else:
                while min_q and not visit[min_q[0][1]]:
                    heapq.heappop(min_q)

                if min_q:
                    visit[min_q[0][1]] = False
                    heapq.heappop(min_q)

    while max_q and not visit[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visit[min_q[0][1]]:
        heapq.heappop(min_q)

    if max_q and min_q:
        print(-max_q[0][0],min_q[0][0])
    else:
        print("EMPTY")

# Pass