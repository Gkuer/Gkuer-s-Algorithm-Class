from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

orders = []
for i in maps:
    if not orders or orders[-1] < i:
        orders.append(i)
    else:
        orders[bisect_left(orders,i)] = i

print(len(orders))

# Pass