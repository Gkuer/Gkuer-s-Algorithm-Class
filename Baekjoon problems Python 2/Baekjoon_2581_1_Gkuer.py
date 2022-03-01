import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

maps = [2,3]
for i in range(4,15000):
    for j in maps:
        if i % j == 0:
            break
    else:
        maps.append(i)

sub_ans, ans, flag = 0, 0, 0
maps = deque(maps)
while True:
    a = maps.popleft()
    if a > m:
        break

    if not flag and n <= a:
        sub_ans = a
        flag = 1
        ans += a
    elif n <= a:
        ans += a

if sub_ans == 0 and ans == 0:
    print(-1)
else:
    print(ans)
    print(sub_ans)

# Pass