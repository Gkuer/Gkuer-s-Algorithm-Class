t = int(input())
for tc in range(1,t+1):
    n, time, chicken = map(int, input().split())
    maps = list(map(int, input().split()))
    maps = sorted(maps)
    temps = []
    ans = "Possible"
    point = time
    while n >= 0:
        for i in range(chicken):
            temps.append(time)

        n -= chicken
        time += point

    while maps and temps:
        a = temps.pop(0)
        b = maps.pop(0)
        if a > b:
            ans = "Impossible"
            break

    print("#{} {}".format(tc, ans))

# Success
