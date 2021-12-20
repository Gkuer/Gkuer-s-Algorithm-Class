n = int(input())

start = 1
ans = 1
cnt = 6
while n > start:
    ans += 1
    start += cnt
    cnt += 6
print(ans)

# Pass