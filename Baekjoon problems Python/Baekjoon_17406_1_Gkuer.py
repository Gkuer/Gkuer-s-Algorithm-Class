import sys
from itertools import permutations
import copy
input = sys.stdin.readline

r, c, k = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(r)]
rotation = []
for i in range(k):
    rotation.append(list(map(int,input().split())))

rotation_per = list(permutations(rotation,k))
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
ans = sys.maxsize

for i in rotation_per:
    temps = copy.deepcopy(maps)
    # Rotation
    for z in i:
        idx, idy, s = z
        s += 1
        for b in range(s):
            now_x = idx - s + b
            now_y = idy - s + b
            temper = temps[now_x][now_y]
            now_dir = 0
            next_x, next_y = -1, -1
            while True:
                next_x = now_x + dirs[now_dir][0]
                next_y = now_y + dirs[now_dir][1]
                if idx-s+b <= next_x < idx+s-b-1 and idy-s+b <= next_y < idy + s-b -1:
                    temps[next_x][next_y], temper = temper, temps[next_x][next_y]

                else:
                    now_dir += 1
                    now_dir = now_dir % 4
                    next_x = now_x + dirs[now_dir][0]
                    next_y = now_y + dirs[now_dir][1]
                    if idx - s + b <= next_x < idx + s - b-1 and idy - s + b <= next_y < idy + s - b-1:
                        temps[next_x][next_y], temper = temper, temps[next_x][next_y]

                now_x, now_y = next_x, next_y

                if (now_x == idx - s + b) and (now_y == idy - s + b):
                    break

    # Finish Rotation
    for j in range(r):
        total = 0
        for y in range(c):
            total += temps[j][y]
        ans = min(total, ans)

print(ans)

# Success