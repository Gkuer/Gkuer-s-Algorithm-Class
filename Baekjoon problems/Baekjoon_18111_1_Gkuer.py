import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
time, height = sys.maxsize, 0

for i in range(257):
    put = dig = 0 # 블록놓기(1), 블록 파기(2)
    for r in range(n):
        for c in range(m):
            if maps[r][c] > i:
                dig += maps[r][c]-i
            else:
                put += i-maps[r][c]
    if put > dig+b:
        continue
    subtime = put + dig*2
    if time >= subtime:
        time = subtime
        height = i

print(time,height)

# Pass