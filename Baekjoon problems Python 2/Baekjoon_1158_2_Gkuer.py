from collections import deque

n, m = map(int,input().split())
maps = [i for i in range(1,n+1)]

maps = deque(maps)

cnt = 0
ans = "<"
while maps:
    val = maps.popleft()
    cnt += 1

    if cnt % m == 0:
        ans += str(val) + ", "
    else:
        maps.append(val)

print(ans[:-2] + ">")

# Pass