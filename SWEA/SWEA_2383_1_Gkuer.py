import copy
import sys
input = sys.stdin.readline
from collections import deque

dirs = [(0,1),(1,0),(-1,0),(0,-1)]
def bfs(idx,idy,mode):
    q = deque()
    q.append([idx,idy,2])
    while q:
        r, c, cnt = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < n:
                if temps[nr][nc][mode] == 0 and maps[nr][nc] < 2:
                    if maps[nr][nc] == 1:
                        temps[nr][nc][mode] = maps[idx][idy] + cnt
                        q.append([nr,nc,cnt+1])

                    else:
                        temps[nr][nc][mode] = -1
                        q.append([nr,nc,cnt+1])

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input().split())) for _ in range(n)]
    temps = [[[0,0] for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for x in range(n):
            if maps[i][x] >=2:
                bfs(i,x,flag)
                flag += 1

    ans_list = []
    for i in range(n):
        for x in range(n):
            if temps[i][x][0] > 0  or temps[i][x][1] > 0:
                ans_list.append(temps[i][x])

    time = 0
    cnt1 = []
    cnt2 = []
    while ans_list or cnt1 or cnt2:
        time += 1
        temp_list = []

        for i in range(len(ans_list)):
            flag = False

            if ans_list[i][0] == time and (len(cnt1) + len(cnt2) < 3):
                cnt1.append(1)
                flag = True

            if ans_list[i][1] == time and (len(cnt1) + len(cnt2) < 3) and not flag:
                cnt2.append(1)
                flag = True

            if ans_list[i][0] == time and (len(cnt1) + len(cnt2) >= 3):
                ans_list[i][0] += 1

            if ans_list[i][1] == time and (len(cnt1) + len(cnt2) >= 3):
                ans_list[i][1] += 1

            if not flag:
                temp_list.append(ans_list[i])


        cnt1_temp = []
        cnt2_temp = []
        for i in range(len(cnt1)):
            cnt1[i] -= 1
            if cnt1[i] == 0:
                pass
            else:
                cnt1_temp.append(cnt1[i])

        for x in range(len(cnt2)):
            cnt2[x] -= 1
            if cnt2[x] == 0:
                pass
            else:
                cnt2_temp.append(cnt2[x])

        ans_list = copy.deepcopy(temp_list)
        cnt1 = copy.deepcopy(cnt1_temp)
        cnt2 = copy.deepcopy(cnt2_temp)
    print("#{} {}".format(tc,time))

# Fail: Wrong Answer