import sys
input = sys.stdin.readline
from collections import deque
def BFS(birus):
    q = deque([birus])
    stack = [birus]
    cnt = 1
    while q:
        now = q.popleft()
        for w in range(computer+1):
            if temps[now][w] and w not in stack:
                q.append(w)
                stack.append(w)
                cnt += 1
    return cnt

computer = int(input())
birus = int(input())
bir = 1

maps = [list(map(int,input().split())) for _ in range(birus)]
temps = [[False]*(computer+1) for _ in range(computer+1)]

for i,x in maps:
    temps[i][x] = temps[x][i] = True

print(BFS(bir)-1)

# Pass