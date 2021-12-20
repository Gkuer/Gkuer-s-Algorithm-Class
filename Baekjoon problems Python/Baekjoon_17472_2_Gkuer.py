import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs(idx,idy,flag):
    q = deque()
    q.append([idx,idy])
    maps[idx][idy] = flag

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = flag
                    q.append([nr,nc])

def go(idx, idy, start):
    for i in range(4):
        nr = idx + dirs[i][0]
        nc = idy + dirs[i][1]
        if 0 <= nr < n and 0 <= nc < m:
            if maps[nr][nc] == 0:
                flag = False
                point = 0
                while maps[nr][nc] == 0:
                    nr += dirs[i][0]
                    nc += dirs[i][1]
                    if 0 <= nr < n and 0 <= nc < m:
                        point += 1
                    else:
                        flag = True
                        break

                if flag or point <= 1:
                    continue

                nodes.append([start,maps[nr][nc],point])

def find(x):
    if union_set[x] == x:
        return x
    return find(union_set[x])

def union(x,y):
    if x < y:
        union_set[y] = x
    else:
        union_set[x] = y

cnt = 2
for i in range(n):
    for x in range(m):
        if maps[i][x] == 1:
            bfs(i,x,cnt)
            cnt += 1

nodes = []
for i in range(n):
    for x in range(m):
        if maps[i][x] != 0:
            go(i,x,maps[i][x])

# print(*maps,sep="\n")
# print(nodes)

# Kruskal
nodes = sorted(nodes,key= lambda x: x[2])
union_set = [0,0] + [i for i in range(2,cnt)]
# print(union_set)

subans = 0
ans = 0
for s, g, v in nodes:
    a, b = find(s), find(g)
    if a != b:
        union(a,b)
        ans += v
        subans += 1

if subans == cnt-2-1:
    print(ans) if ans != 0 else print(-1)
else:
    print(-1)


# Pass