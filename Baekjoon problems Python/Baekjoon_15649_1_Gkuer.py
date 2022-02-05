import sys
input = sys.stdin.readline

def comb(k,val):
    if k == m:
        print(*val)
        return

    for i in range(1,n+1):
        if not maps[i]:
            maps[i] = 1
            comb(k+1,val+[i])
            maps[i] = 0

n, m = map(int,input().split())
maps = [0] * (n+1)
comb(0,[])

# Pass