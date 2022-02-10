import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
ans = 2500

for i in range(n-8+1):
    for j in range(m-8+1):

        w_cnt, b_cnt = 0, 0

        for k in range(8):
            for l in range(8):
                if (k+l) % 2 == 0:
                    if maps[i+k][j+l] != "W":
                        w_cnt += 1
                    if maps[i+k][j+l] != "B":
                        b_cnt += 1
                else:
                    if maps[i+k][j+l] != "W":
                        b_cnt += 1
                    if maps[i+k][j+l] != "B":
                        w_cnt += 1

        ans = min(ans,w_cnt,b_cnt)

print(ans)

# Pass