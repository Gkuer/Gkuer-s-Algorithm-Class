import sys
input = sys.stdin.readline

goal = list(map(int,input().split()))
maps = [0,0,0]
limit = [15,28,19]

cnt = 0
while maps != goal:
    for i in range(3):
        maps[i] += 1

    for i in range(3):
        if maps[i] > limit[i]:
            maps[i] = 1

    cnt += 1

print(cnt)

# Pass