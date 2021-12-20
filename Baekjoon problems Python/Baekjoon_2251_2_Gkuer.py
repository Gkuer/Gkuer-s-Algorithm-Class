import sys
from collections import deque
input = sys.stdin.readline

def bfs(fx,fy,fz):
    q = deque()
    q.append([fx,fy,fz])

    while q:
        x,y,z = q.popleft()
        if [x,y,z] in visited:
            continue
        visited.append([x,y,z])

        if x == 0:
            ans.append(z)

        if x+y >= b:
            q.append([x-(b-y),b,z])
        else:
            q.append([0,x+y,z])

        if x+z >= c:
            q.append([x-(c-z),y,c])
        else:
            q.append([0,y,x+z])

        if y+x >= a:
            q.append([a,y-(a-x),z])
        else:
            q.append([x+y, 0, z])

        if y+z >= c:
            q.append([x, y-(c-z), c])
        else:
            q.append([x,0,y+z])

        if z+x >= a:
            q.append([a,y,z-(a-x)])
        else:
            q.append([x+z,y,0])

        if z+y >= b:
            q.append([x,b,z-(b-y)])
        else:
            q.append([x,y+z,0])



a,b,c = map(int,input().split())
visited = []
ans = []
bfs(0,0,c)
ans = list(set(ans))
ans = sorted(ans)
print(*ans)

# Pass