t= int(input())
for tc in range(1,t+1):
    n, maps = input().split()
    temps = ""

    for x in range(len(maps)):
        for i in range(int(n)):
            temps += maps[x]

    print(temps)

# Pass