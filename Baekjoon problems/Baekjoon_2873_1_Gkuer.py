import sys
input = sys.stdin.readline

r, c = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(r)]

if r % 2 == 1:
    print(("R"*(c-1) + "D" + "L"*(c-1) + "D")*(r//2) + "R"*(c-1))
elif c % 2 == 1:
    print(("D"*(r-1) + "R" + "U"*(r-1) + "R")*(c//2) + "D"*(r-1))
else:
    mn = 1000
    pos = [0,0]
    for i in range(r):
        if i % 2:
            for j in range(0,c,2):
                if mn > maps[i][j]:
                    mn = maps[i][j]
                    pos = [i,j]
        else:
            for j in range(1,c,2):
                if mn > maps[i][j]:
                    mn = maps[i][j]
                    pos = [i,j]

    res = ("D"*(r-1) + "R" + "U"*(r-1) + "R") * (pos[1]//2)
    idx, idy = 0, 2*(pos[1]//2)
    max_idy = 2*(pos[1]//2) + 1
    while idy != max_idy or idx != r-1:
        if idy < max_idy and [idx,max_idy] != pos:
            idy += 1
            res += "R"
        elif idy == max_idy and [idx,max_idy-1] != pos:
            idy -= 1
            res += "L"
        if idx != r-1:
            idx += 1
            res += "D"

    res += ("R" + "U"*(r-1) + "R" + "D"*(r-1))*((c-1-pos[1])//2)

    print(res)

# Pass