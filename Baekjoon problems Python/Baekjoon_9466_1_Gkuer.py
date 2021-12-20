import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def dfs(start, now, team, li):
    if maps[now] == start:
        for i in li:
            temps[i] = team
        return

    elif now == maps[now]:
        for i in li:
            temps[i] = -1
        temps[now] = num
        return False

    return dfs(start, maps[now],team, li+[maps[now]])

t = int(input())
for tc in range(1,t+1):
    n = int(input().strip())
    maps = [0] + list(map(int,input().strip().split()))
    temps = [0]*(n+1)
    num = 1
    for i in range(1,n+1):
        if temps[i] == 0:
            dfs(i,i,num,[i])
            num += 1

    cnt = 0
    for i in temps:
        if i == -1:
            cnt += 1
    print(cnt)

# Fail: Memory Over