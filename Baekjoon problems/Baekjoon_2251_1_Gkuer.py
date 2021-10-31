import sys
input = sys.stdin.readline
import copy

sys.setrecursionlimit(10**6)
def dfs(now,pos):
    global ans
    if now not in visited:
        visited.append(now)
    else:
        return

    if now[0] == 0:
        ans.append(now[2])

    for i in range(3):
        if i != pos:
            new = copy.deepcopy(now)
            # target의 물을 가득 채울 수 있을 때
            if new[i]+new[pos] >= cap[i]:
                new[pos] = new[pos] - (cap[i]-new[i])
                new[i] = cap[i]
                dfs(new,i)
                if new[pos] > 0:
                    visited.remove(new)
                    dfs(new,pos)

            # 나의 물을 비울 수 있을 때
            elif new[pos] <= cap[i]-new[i]:
                new[i] = new[pos] + new[i]
                new[pos] = 0
                dfs(new,i)

    return


cap = list(map(int,input().split()))
visited = []
ans = []

dfs([0,0,cap[2]],2)

ans = list(set(ans))
ans = sorted(ans)
print(*ans)

# Fail: Momory Over