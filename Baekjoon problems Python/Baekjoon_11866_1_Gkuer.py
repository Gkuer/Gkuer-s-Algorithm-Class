import sys
input = sys.stdin.readline

n, k = map(int,input().split())
maps = [i for i in range(1,n+1)]
ans = []
cnt = 1
while maps:
    a = maps.pop(0)

    if cnt%k == 0:
        ans.append(a)
    else:
        maps.append(a)
    cnt += 1


print("<", end="")
print(*ans,sep=", ", end="")
print(">")

# Pass