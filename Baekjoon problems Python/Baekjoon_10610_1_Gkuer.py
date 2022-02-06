n = list(input().strip())
n.sort(reverse=True)
sm = 0
for i in n:
    sm += int(i)

if "0" not in n or sm % 3 != 0:
    print(-1)
else:
    print("".join(n))

# Pass