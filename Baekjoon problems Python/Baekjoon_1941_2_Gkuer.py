import sys
from itertools import combinations
input = sys.stdin.readline


temps = [i for i in range(25)]
maps = []
for i in range(5):
    maps += list(input().strip())

comb = list(combinations(temps,7))

ans = 0
for i in range(len(comb)):
    li = comb[i]
    now = li[0]
    subans = [maps[now]]
    for x in li[1:]:
        if (x == now+1 or x == now-1) and x // 5 == now // 5: # 좌우
            subans.append(maps[x])
        elif x % 5 == now % 5 and (x//5 == now//5+1 or x//5 == now//5-1): # 상하
            subans.append(maps[x])
        else:
            break

        if subans.count("Y") >= 5:
            break

        now = x

    else:
        if subans.count("S") >= 4:
            print(li)
            print(subans)
            ans += 1

print(ans)

# Fail: Wrong Answer