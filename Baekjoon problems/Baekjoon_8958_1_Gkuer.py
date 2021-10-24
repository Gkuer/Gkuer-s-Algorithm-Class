t = int(input())
for tc in range(t):
    maps = input()
    ans = 0
    cnt = 0
    for i in maps:
        if i == "O":
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)
# Pass