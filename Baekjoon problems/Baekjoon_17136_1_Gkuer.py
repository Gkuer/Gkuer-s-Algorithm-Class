import sys
input = sys.stdin.readline

def check():
    for i in range(10):
        for x in range(10):
            if maps[i][x] == 1:
                return True
    else:
        return False

def get_mx(): # If paper is possible, return mx else return 0
    global paper
    mx = 0
    mx_idx, mx_idy = 0, 0

    for r in range(10):
        for c in range(10):
            now = 5
            if maps[r][c] == 1:
                while mx < now: # Check possible put paper in
                    flag = False
                    for i in range(now):
                        for x in range(now):
                            nr = r + i
                            nc = c + x
                            if 0 <= nr < 10 and 0 <= nc < 10:
                                if maps[nr][nc] == 0: # Can't paper size, Go next paper
                                    flag = True
                                    break

                            else: # Can't paper size, Go next paper
                                flag = True
                                break

                        if flag:
                            now -= 1
                            break

                    else: # Success put in paper
                        if paper[now]:
                            mx = now
                            mx_idx, mx_idy = r, c

                        else:
                            now -= 1

    return [mx, mx_idx, mx_idy]

maps = [list(map(int, input().split())) for _ in range(10)]
paper = [0,5,5,5,5,5]
ans = 0

while check(): # If 1 in maps, Keep loop
    mx, mx_idx, mx_idy = get_mx()
    if mx:
        ans += 1
        for r in range(mx):
            for c in range(mx):
                nr = mx_idx + r
                nc = mx_idy + c
                maps[nr][nc] = 0
                paper[mx] -= 1
    else:
        ans = -1
        break

print(ans)

# Fail: Wrong answer