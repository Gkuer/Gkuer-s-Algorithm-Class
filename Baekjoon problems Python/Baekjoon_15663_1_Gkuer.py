import sys
input = sys.stdin.readline

def find():
    if len(res) == m:
        if tuple(res) not in ans:
            print(*res)
            ans[tuple(res)] = 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            res.append(maps[i])
            find()
            visited[i] = 0
            res.pop()

n, m = map(int,input().split())
maps = list(map(int,input().split()))
maps.sort()
visited = [0]*n
ans = {}
res = []
find()

# Pass
