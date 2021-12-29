import sys
input = sys.stdin.readline

n = int(input())
res = 1
for i in range(1,n+1):
    res *= i

res = str(res)
ans = 0
for x in reversed(res):
    if x == '0':
        ans += 1
    else:
        break

print(ans)

# Pass