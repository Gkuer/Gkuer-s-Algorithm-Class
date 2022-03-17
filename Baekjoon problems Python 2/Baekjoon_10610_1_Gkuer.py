n = input().strip()

res = "".join(sorted(n,reverse=True))

if (sum(list(map(int,res))) % 3 == 0) and res[-1] == "0":
    print(res)
else:
    print(-1)

# Pass