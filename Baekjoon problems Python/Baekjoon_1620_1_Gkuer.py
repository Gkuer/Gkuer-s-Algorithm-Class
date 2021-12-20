import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [input().strip() for i in range(n)]
for i in range(m):
    a = input().strip()
    try:
        a = int(a)
        print(maps[a])
    except:
        print(maps.index(a)+1)