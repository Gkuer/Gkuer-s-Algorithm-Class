#1
def solution(k, m, names, amounts):
    answer = 0
    l = len(names)
    for i in range(l):
        names[i] = names[i].lower()

    maps = {}
    for i in range(l):
        flag = False
        if names[i] not in maps:
            maps = {}
            maps[names[i]] = 1
        else:
            maps[names[i]] += 1
            if maps[names[i]] >= k:
                flag = True
                answer += 1

        if not flag and amounts[i] >= m:
            answer += 1

    return answer

# 2
def solution(a, b, duration, distance):
    answer = 987654321

    where = 0
    while where <= distance:
        a_min_time = a[0] + where
        b_min_time = b[0] + distance-where

        a_home_start_time = max(a_min_time,b_min_time) + duration
        b_home_start_time = max(a_min_time,b_min_time) + duration

        a_home_end_time = a_home_start_time + where
        b_home_end_time = b_home_start_time + distance-where

        if a_home_end_time <= a[1] and b_home_end_time <= b[1]:
            answer = min(answer, max(a_min_time,b_min_time))

        where += 1

    if answer == 987654321:
        answer = -1

    return answer

#3
def solution(ledgers):
    answer = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    maps = []
    for ledger in ledgers:
        month = int(ledger[0:2])
        day = int(ledger[3:5])
        r = int(ledger[6]) * 0.01
        money = int(ledger[8:])

        tday = 0
        for i in range(month - 1):
            tday += days[i]
        tday += day

        if money >= 0:
            maps.append([tday, money, r])

        else:
            money = -money
            while money > 0:
                bank_day, bank_money, bank_r = maps.pop()
                remainder = bank_money - money
                if remainder < 0:
                    answer += int((bank_money * bank_r) * ((tday - bank_day) / 365))
                    money = -remainder
                else:
                    answer += int((money * bank_r) * ((tday - bank_day) / 365))
                    maps.append([bank_day,remainder,bank_r])
                    money = 0

    while maps:
        bank_day, bank_money, bank_r = maps.pop()
        answer += int((bank_money * bank_r) * ((365 - bank_day) / 365))

    return answer

# 4
def solution(s, times):
    maps = []
    s = s.split(":")
    s = list(map(int,s))
    maps.append(s)
    l = len(times)

    for i in range(l):
        year, month, day, hour, minute, second = maps[-1]
        lst = list(map(int,times[i].split(":")))
        temps = list(map(int,[year, month, day + lst[0], hour + lst[1], minute + lst[2], second + lst[3]]))

        if temps[5] >= 60:
            val = temps[5]//60
            temps[4] += val
            temps[5] = temps[5] - val*60

        if temps[4] >= 60:
            val = temps[4]//60
            temps[3] += val
            temps[4] = temps[4] - val*60

        if temps[3] >= 24:
            val = temps[3]//24
            temps[2] += val
            temps[3] = temps[3] - val*24

        while temps[2] > 30:
            temps[2] -= 30
            temps[1] += 1

        while temps[1] > 12:
            temps[1] -= 12
            temps[0] += 1

        maps.append(temps)


    maps.sort()
    temps = []
    for i in range(6):
        temps.append(maps[-1][i] - maps[0][i])

    sm = 0
    for i in range(3):
        if i == 0:
            sm += temps[i]*360
        elif i == 1:
            sm += temps[i]*30
        elif i == 2:
            sm += temps[i]

    start = s[:3]
    flag = False
    for i in range(sm):
        year, month, day = start
        day += 1
        if day >= 31:
            day = 1
            month += 1

        if month >= 13:
            month = 1
            year += 1

        for j in maps:
            if [year, month, day] == j[:3]:
                break
        else:
            flag = True
            break

        start = [year, month, day]

    if flag:
        answer = [0,sm+1]
    else:
        answer = [1,sm+1]
    return answer

# 5
from collections import deque

def solution(grids):
    answer = []
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    for maps in grids:
        sub_ans = True
        maps = list(map(list,maps))
        n = len(maps)
        m = len(maps[0])

        first_flag = False
        r, c = 0, 0
        for i in range(n):
            for j in range(m):
                if maps[i][j] == "X":
                    r, c = i, j
                    first_flag = True
                    break
            if first_flag:
                break

        if not first_flag:
            sub_ans = False


        third_flag = False
        for i in range(n):
            for j in range(m):
                if maps[i][j] == ".":
                    third_flag = True
                    break
            if third_flag:
                break

        if not third_flag:
            sub_ans = False

        q = deque()
        q.append([r,c])
        maps[r][c] = "O"
        mn_r, mn_c, mx_r, mx_c = r, c, r, c

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dirs[i][0]
                nc = c + dirs[i][1]
                if 0 <= nr < n and 0 <= nc < m:
                    if maps[nr][nc] == "X":
                        maps[nr][nc] = "O"
                        q.append([nr,nc])
                        mn_r = min(mn_r, nr)
                        mn_c = min(mn_c, nc)
                        mx_r = max(mx_r, nr)
                        mx_c = max(mx_c, nc)

        if maps[mn_r][mn_c] != "O" or maps[mx_r][mx_c] != "O":
            sub_ans = False

        for i in range(n):
            for j in range(m):
                if maps[i][j] == "X":
                    sub_ans = False

        mini_r, mini_c, maxi_r, maxi_c = 501, 501, -1, -1
        second_flag = False
        if sub_ans:
            for i in range(mn_r, mx_r):
                for j in range(mn_c, mx_c):
                    if maps[i][j] == ".":
                        second_flag = True
                        mini_r = min(mini_r, i)
                        mini_c = min(mini_c, j)
                        maxi_r = max(maxi_r, i)
                        maxi_c = max(maxi_c, j)

            if not second_flag:
                sub_ans = False

            for i in range(mini_r, maxi_r):
                for j in range(mini_c, maxi_c):
                    if maps[i][j] != ".":
                        sub_ans = False

        answer.append(sub_ans)
    return answer