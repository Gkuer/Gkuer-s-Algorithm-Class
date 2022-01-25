import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
maps = [[-1, 0] for _ in range(100001)]  # 걸린시간, 경우의 수

q = deque([])
q.append(n)

maps[n][0] = 0
maps[n][1] = 1

while q:
    pos = q.popleft()

    for next in [pos+1, pos-1, pos*2]:
        if 0 <= next <= 100000:
            if maps[next][0] == - 1:
                maps[next][0] = maps[pos][0] + 1
                maps[next][1] = maps[pos][1]
                q.append(next)

            elif maps[next][0] == maps[pos][0] + 1:
                maps[next][1] += maps[pos][1]

print(maps[k][0])
print(maps[k][1])

# Pass