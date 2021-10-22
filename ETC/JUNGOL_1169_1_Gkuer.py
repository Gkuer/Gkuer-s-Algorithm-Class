def perm1(d):
    if d > n:
        print(*temps[1:])
        return

    for i in range(1, 7):
        temps[d] = i
        perm1(d+1)

def perm2(d):
    if d > n:
        print(*temps[1:])
        return
    for i in range(temps[d-1], 7):
        temps[d] = i
        perm2(d+1)


def perm3(d):
    if d > n:
        print(*temps[1:])
        return
    for i in range(1,7):
        if not visited[i]:
            visited[i] = 1
            temps[d] = i
            perm3(d+1)
            visited[i] = 0

n, i = map(int, input().split())
visited = [0] * 7
temps = [0] * (n + 1)
if i == 1:
    perm1(1)
elif i == 2:
    temps[0] = 1
    perm2(1)
else:
    perm3(1)

# Pass