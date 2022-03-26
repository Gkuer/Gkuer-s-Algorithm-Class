import copy
from collections import deque

def solution(n, m, room, bath):
    global answer, pres

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    def check1(check_maps1):
        already = []
        ready = []
        for i in range(n):
            for j in range(m):
                if check_maps1[i][j] and check_maps1[i][j] not in already:
                    already.append(check_maps1[i][j])
                    ready.append([i,j])

        for i in range(len(already)):
            if already[i] < 100:
                rng_x, rng_y = 2, 2
            elif already[i] < 200:
                rng_x, rng_y = 2, 1
            else:
                rng_x, rng_y = 1, 2

            flag = False
            for r in range(rng_x):
                for c in range(rng_y):
                    for j in range(4):
                        nr = ready[i][0] + r + dirs[j][0]
                        nc = ready[i][1] + c + dirs[j][1]
                        if 0 <= nr < n and 0 <= nc < m:
                            if check_maps1[nr][nc] == 0:
                                flag = True
                                break
                    if flag:
                        break
                if flag:
                    break
            else:
                return False

        return True

    def check2(check_maps2):
        flag = False
        for i in range(n):
            for j in range(m):
                if check_maps2[i][j] == 0:
                    ini_x = i
                    ini_y = j
                    flag = True
                    break
            if flag:
                break

        if not flag:
            return False

        q = deque()
        q.append([ini_x, ini_y])
        check_maps2[ini_x][ini_y] = -1
        while q:
            r, c = q.popleft()
            for k in range(4):
                nr = r + dirs[k][0]
                nc = c + dirs[k][1]
                if 0 <= nr < n and 0 <= nc < m:
                    if check_maps2[nr][nc] == 0:
                        check_maps2[nr][nc] = -1
                        q.append([nr,nc])

        for i in range(n):
            for j in range(m):
                if check_maps2[i][j] == 0:
                    return False

        return True

    def check3(check_maps3):
        for i in range(n):
            for j in range(m):
                if check_maps3[i][j] == 0:
                    for k in range(4):
                        nr = i + dirs[k][0]
                        nc = j + dirs[k][1]
                        if not(0 <= nr < n and 0 <= nc < m):
                            return True
        return False

    def find(maps, mode, cnts):
        global answer, pres

        if cnts == [0,0,0]:
            if maps not in pres:
                pres.append(copy.deepcopy(maps))
                if check1(copy.deepcopy(maps)) and check2(copy.deepcopy(maps)) and check3(copy.deepcopy(maps)):
                    answer += 1
                return

        if mode == 0:
            x_rng, y_rng = 2, 2
        elif mode == 1:
            x_rng, y_rng = 2, 1
        else:
            x_rng, y_rng = 1, 2

        for r in range(n):
            for c in range(m):
                flag = 0
                for i in range(x_rng):
                    for j in range(y_rng):
                        nr = r + i
                        nc = c + j
                        if 0 <= nr < n and 0 <= nc < m:
                            if maps[nr][nc] == 0:
                                flag += 1

                if flag == x_rng*y_rng:
                    temps = copy.deepcopy(maps)
                    for i in range(x_rng):
                        for j in range(y_rng):
                            nr = r + i
                            nc = c + j
                            temps[nr][nc] = 100*mode + cnts[mode] + 1

                    cnts[mode] -= 1
                    next = 0
                    for i in range(3):
                        if cnts[i]:
                            next = i
                            break

                    find(temps, next, cnts)
                    cnts[i] += 1
                    for i in range(x_rng):
                        for j in range(y_rng):
                            nr = r + i
                            nc = c + j
                            temps[nr][nc] = 0

    answer = 0
    inis = [[0]*m for _ in range(n)]
    pres = []

    find(inis,0,[room,0,1])

    return answer

print(solution(4,5,3,1))