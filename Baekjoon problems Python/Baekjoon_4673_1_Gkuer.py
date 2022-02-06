maps = [i for i in range(1,10001)]
ans = []
for i in maps:
    temp = i
    for j in str(i):
        temp += int(j)
    ans.append(temp)

ans = set(ans)

for i in maps:
    if i not in ans:
        print(i)

# Pass