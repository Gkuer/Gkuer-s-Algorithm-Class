maps = list(map(int, input().split()))

pre = maps[0]
if pre > maps[1]:
    flag = "descending"
else:
    flag = "ascending"

for i in maps[1:]:
    if i > pre:
        if flag == "descending":
            print("mixed")
            break
    else:
        if flag == "ascending":
            print("mixed")
            break
    pre = i

else:
    print(flag)

# Pass