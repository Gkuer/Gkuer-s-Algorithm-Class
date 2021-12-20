word = input()
ans = 0
cnt = 1
for i in word:
    if i == " ":
        cnt += 1
    else:
        if cnt:
            ans += 1
            cnt = 0
print(ans)

# Pass