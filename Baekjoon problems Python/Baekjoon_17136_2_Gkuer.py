import sys
input = sys.stdin.readline

def func(idx,idy,cnt):
    global paper, ans, maps

    if idy >= 10:
        func(idx+1, 0, cnt)
        return
    if idx >= 10:
        ans = min(ans, cnt)
        return

    if maps[idx][idy] == 1:
        for x in range(5):
            flag = False

            if paper[x] >= 5:
                continue
            if idx + x >= 10 or idy + x >= 10:
                continue

            for i in range(idx, idx+x+1):
                for j in range(idy, idy+x+1):
                    if maps[i][j] == 0:
                        flag = True
                        break
                if flag:
                    break

            if not flag:
                for i in range(idx, idx+x+1):
                    for j in range(idy, idy+x+1):
                        maps[i][j] = 0
                paper[x] += 1
                func(idx, idy+x+1, cnt+1)
                paper[x] -= 1
                for i in range(idx, idx+x+1):
                    for j in range(idy, idy+x+1):
                        maps[i][j] = 1
    else:
        func(idx,idy+1,cnt)

maps = [list(map(int,input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
func(0, 0, 0)
print(ans) if ans != sys.maxsize else print(-1)

# Success