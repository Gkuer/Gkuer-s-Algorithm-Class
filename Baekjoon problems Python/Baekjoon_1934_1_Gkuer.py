t = int(input())
for tc in range(1, t+1):
    a, b = map(int,input().split())
    c, d = a, b
    while c != 0:
        d = d%c
        c,d = d,c

    gcd = d
    lcm = a*b // gcd

    print(lcm)

# Pass