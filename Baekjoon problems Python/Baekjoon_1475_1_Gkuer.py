maps = list(map(int,input()))

cnt = len(maps)
t = 0
while cnt:
    t += 1
    temps = [0] * 10
    for i in range(len(maps)):
        if maps[i] != -1:
            if not temps[maps[i]]:
                temps[maps[i]] = 1
                cnt -= 1
                maps[i] = -1

            elif maps[i] == 6 or maps[i] == 9:
                if not temps[6] or not temps[9]:
                    if maps[i] == 6:
                        temps[9] = 1
                        cnt -= 1
                        maps[i] = -1
                    else:
                        temps[6] = 1
                        cnt -= 1
                        maps[i] = -1
print(t)

# Pass