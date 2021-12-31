import sys
input = sys.stdin.readline

def recursion(idx,idy,size):
    color = maps[idx][idy]
    for i in range(idx,idx+size):
        for j in range(idy,idy+size):
            if maps[i][j] != color:
                recursion(idx,idy,size//2)
                recursion(idx,idy+size//2,size//2)
                recursion(idx+size//2,idy,size//2)
                recursion(idx+size//2,idy+size//2,size//2)
                return
    result.append(color)

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

result = []
recursion(0,0,n)

print(result.count(0))
print(result.count(1))

# Pass