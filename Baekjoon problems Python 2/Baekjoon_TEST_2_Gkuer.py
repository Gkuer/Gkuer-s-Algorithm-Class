from collections import deque

dirs = [(0,1),(0,-1)]
dirs_x = [(1,0),(-1,0)]

def find(dense):
    temps = [[0]*m for _ in range(n)]
    temps[start_x][start_y] = 1
    q = deque()
    q.append([start_x,start_y])
    while q:
        x, y = q.popleft()
        for i in range(2):
            nr = x + dirs[i][0]
            nc = y + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if not temps[nr][nc]:
                    temps[nr][nc] = 1
                    if maps[nr][nc] == 1:
                        q.append([nr,nc])
                    elif maps[nr][nc] == 3:
                        return True

        for j in range(1,dense+1):
            for i in range(2):
                nr = x + dirs_x[i][0]*j
                nc = y + dirs_x[i][1]*j
                if 0 <= nr < n and 0 <= nc < m:
                    if not temps[nr][nc]:
                        temps[nr][nc] = 1
                        if maps[nr][nc] == 1:
                            q.append([nr,nc])
                        elif maps[nr][nc] == 3:
                            return True

    return False


t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                start_x, start_y = i, j

    step = 0
    while True:
        res = find(step)
        if res:
            break
        step += 1

    print("#{} {}".format(tc, step))