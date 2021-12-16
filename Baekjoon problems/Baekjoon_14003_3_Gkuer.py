from bisect import bisect_left
import sys
input = sys.stdin.readline

def bin_search():
    s, e = 0, len
n = int(input())
maps = list(map(int,input().split()))

orders = []
new_maps = []
for i in maps:
    if not orders or orders[-1] < i:
        orders.append(i)
        new_maps.append([len(orders)-1,i])
    else:
        orders[bisect_left(orders,i)] = i
        new_maps.append([bisect_left(orders,i),i])


ans = []
ordering = len(orders)-1
for i in range(n-1,-1,-1):
    if new_maps[i][0] == ordering:
        ans.append(new_maps[i][1])
        ordering -= 1

print(len(ans))
print(*ans[::-1])

# Pass