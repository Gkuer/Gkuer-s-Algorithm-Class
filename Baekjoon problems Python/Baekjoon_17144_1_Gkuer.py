import sys
input = sys.stdin.readline
dirs_up = [(0,1),(-1,0),(0,-1),(1,0)]
dirs_down = [(0,1),(1,0),(0,-1),(-1,0)]

def simulation1():
    new_maps = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maps[i][j] >= 5:
                cnt = 0
                for k in range(4):
                    nr = i + dirs_up[k][0]
                    nc = j + dirs_up[k][1]
                    if 0 <= nr < r and 0 <= nc < c:
                        if maps[nr][nc] != -1:
                            new_maps[nr][nc] += maps[i][j]//5
                            cnt += 1
                maps[i][j] -= (maps[i][j]//5)*cnt

    for i in range(r):
        for j in range(c):
            maps[i][j] += new_maps[i][j]

def simulation2(idx1,idy1,idx2,idy2):

    position = [idx1,idy1]
    temp = 0
    for i in range(4):
        if i % 2 == 0:
            for j in range(c-1):
                nr = position[0] + dirs_up[i][0]
                nc = position[1] + dirs_up[i][1]
                maps[nr][nc], temp = temp, maps[nr][nc]
                position = [nr, nc]
        else:
            for j in range(idx1):
                nr = position[0] + dirs_up[i][0]
                nc = position[1] + dirs_up[i][1]
                maps[nr][nc], temp = temp, maps[nr][nc]
                position = [nr,nc]

    maps[idx1][idy1] = -1

    position = [idx2, idy2]
    temp = 0
    for i in range(4):
        if i % 2 == 0:
            for j in range(c-1):
                nr = position[0] + dirs_down[i][0]
                nc = position[1] + dirs_down[i][1]
                maps[nr][nc], temp = temp, maps[nr][nc]
                position = [nr, nc]
        else:
            for j in range(r-idx2-1):
                nr = position[0] + dirs_down[i][0]
                nc = position[1] + dirs_down[i][1]
                maps[nr][nc], temp = temp, maps[nr][nc]
                position = [nr, nc]

    maps[idx2][idy2] = -1

r, c, t = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(r)]

pos = []
for i in range(r):
    if maps[i][0] == -1:
        pos.append(i)

while t > 0:
    simulation1()
    simulation2(pos[0],0,pos[1],0)
    t -= 1

ans = 0
for i in range(r):
    for j in range(c):
        ans += maps[i][j]

print(ans+2)

# Pass