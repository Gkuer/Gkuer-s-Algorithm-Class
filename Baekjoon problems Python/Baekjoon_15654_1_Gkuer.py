import sys
input = sys.stdin.readline

def find():
    if len(ans) >= m:
        print(*ans)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            ans.append(maps[i])
            find()
            ans.pop()
            visited[i] = 0

n, m = map(int,input().split())
maps = list(map(int,input().split()))
maps.sort()
visited = [0] * n
ans = []
find()

# Pass