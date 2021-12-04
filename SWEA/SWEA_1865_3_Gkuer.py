import sys
input = sys.stdin.readline

def find(s,val):
    global ans

    if val <= ans:
        return

    if s >= n and val > ans:
        ans = val
        return

    for i in range(n):
        if i not in temps:
            temps[s] = i
            find(s+1,val*maps[s][i]*0.01)
            temps[s] = -1

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [-1]*n
    ans = 0
    find(0,100)

    print("#{} {:0.6f}".format(tc, ans))

# Pass