maps = list(map(int,input().split()))
ans = 0
for i in maps:
    ans += i**2
print(ans % 10)

# Pass