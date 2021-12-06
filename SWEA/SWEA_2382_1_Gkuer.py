import sys
input = sys.stdin.readline
dirs = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]

def go():
    for i in range(len(cells)):
        cells[i][0] = cells[i][0] + dirs[cells[i][3]][0]
        cells[i][1] = cells[i][1] + dirs[cells[i][3]][1]

    res = []
    res_temp = []
    for i in range(len(cells)):
        for x in range(len(res)):
            if cells[i][0] == res[x][0] and cells[i][1] == res[x][1]:
                if res_temp[x] < cells[i][2]:
                    res[x][3] = cells[i][3]
                    res_temp[x] = cells[i][2]
                res[x][2] += cells[i][2]
                break
        else:
            res.append(cells[i])
            res_temp.append(cells[i][2])

    return res

t = int(input())
for tc in range(1,t+1):
    n, m, k = map(int,input().split())
    cells = []
    for _ in range(k):
        cells.append(list(map(int,input().split())))

    while m:
        cells = go()
        for i in range(len(cells)):
            if not(1 <= cells[i][0] <= n-2) or not(1 <= cells[i][1] <= n-2):
                cells[i][2] = cells[i][2] // 2
                if cells[i][3] % 2:
                    cells[i][3] += 1
                else:
                    cells[i][3] -= 1

        m -= 1


    ans = 0
    for i in range(len(cells)):
        ans += cells[i][2]

    print("#{} {}".format(tc,ans))

# Pass