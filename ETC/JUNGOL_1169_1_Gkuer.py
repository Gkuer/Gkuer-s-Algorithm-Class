def perm(d):
    if d > n-1:
        print(*temps)
        return

    for i in range(temps[d-1],7):
        temps[d] = i
        perm(d+1)

n = int(input())
temps = [1] * n
temps[0] = 1
perm(0)