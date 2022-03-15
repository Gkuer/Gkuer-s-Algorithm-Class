import sys
sys.stdin = open("input.txt")

def hunt(old_maps, r=0, c=0, repeat=0, cnt=0):
    global answer
    if cnt >= answer:
        return

    if repeat == m:
        answer = cnt

    for i in range(8):
        maps = old_maps[:]
        step = 0
        if maps[i] == True:
            maps[i] = False
            nr, nc = pos[i]
            step += abs(nr - r) + abs(nc - c)
            if i < 4:
                maps[4 + i] = True
            hunt(maps, nr, nc, repeat + 1, cnt + step)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    bugs = [False for _ in range(8)]
    pos = [[] for _ in range(8)]
    origin = [list(map(int,input().split())) for _ in range(n)]
    m = 0
    for i in range(n):
        for j in range(n):
            if origin[i][j] != 0:
                if origin[i][j] < 0:
                    pos[3 - origin[i][j]] = [i, j]
                    m += 1
                else:
                    bugs[origin[i][j] - 1] = True
                    pos[origin[i][j] - 1] = [i, j]
                    m += 1

    answer = 987654321

    hunt(bugs)
    print(answer)