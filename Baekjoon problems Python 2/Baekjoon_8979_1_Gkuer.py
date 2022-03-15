import sys
input = sys.stdin.readline

n, k = map(int,input().split())
maps = [0] + [0 for _ in range(n)]
for _ in range(n):
    a, b, c, d = map(int,input().split())
    maps[a] = int(b*1000000000001+c*1000001+d)

goal = maps[k]
ans = 1
for i in range(1,n+1):
    if maps[i] > goal:
        ans += 1

print(ans)

# Pass