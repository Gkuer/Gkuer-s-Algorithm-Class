case = 1
while True:
    l, p, v = map(int,input().split())
    if l + p + v == 0:
        break

    answer = 0
    days = v//p
    answer += days*l
    answer += min(l,v-days*p)

    print(f"Case {case}: {answer}")
    case += 1

# Pass