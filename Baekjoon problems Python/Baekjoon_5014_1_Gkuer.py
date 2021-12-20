import sys
input = sys.stdin.readline

def bf(now,cnt):
    global ans
    if now == g:
        ans = cnt
        return

    if now < 1 or now > 1000000:
        return


    if not visited[now]:
        visited[now] = 1
        if now+u <= f:
            bf(now+u,cnt+1)
        if now-d >= 1:
            bf(now-d,cnt+1)


f, s, g, u, d = map(int,input().split())
visited = [0]*1000000
ans = 0
bf(s,0)
print(ans) if ans != 0 else print("use the stairs")

# Fail: Recursion Error & Memory Exceeded