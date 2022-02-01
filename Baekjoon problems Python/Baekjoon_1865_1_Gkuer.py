import sys
input = sys.stdin.readline
inf = 987654321

def bellmanford():

    for i in range(1,n+1):
        for j in range(1,n+1):
            for weight, next in maps[j]:
                if dist[next] > weight + dist[j]:
                    dist[next] = weight + dist[j]
                    if i == n:
                        return True
    return False

t = int(input())
for tc in range(1,t+1):
    n, m, w = map(int,input().split())
    dist = [inf] * (n+1)
    maps = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, t = map(int,input().split())
        maps[s].append((t,e))
        maps[e].append((t,s))

    for _ in range(w):
        s, e, t = map(int,input().split())
        maps[s].append((-t,e))

    res = bellmanford()

    print("YES" if res else "NO")

# Pass