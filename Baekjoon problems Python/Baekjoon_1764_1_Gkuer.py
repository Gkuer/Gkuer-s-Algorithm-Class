import sys
input = sys.stdin.readline

n, m = map(int,input().split())

maps = {}
for i in range(n+m):
    a = input().strip()
    if maps.get(a):
        maps[a] += 1
    else:
        maps[a] = 1

maps = sorted(maps.items(),key=lambda x:x[1])

ans = []
for key, value in reversed(maps):
    if value == 1:
        break
    else:
        ans.append(key)

ans.sort()
print(len(ans))
for i in ans:
    print(i)

# Pass