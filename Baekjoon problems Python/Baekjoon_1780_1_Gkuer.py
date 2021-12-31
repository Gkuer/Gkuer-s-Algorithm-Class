import sys
input = sys.stdin.readline

def recursion(idx,idy,size):
    color = maps[idx][idy]

    for i in range(idx,idx+size):
        for j in range(idy,idy+size):
            if maps[i][j] != color:
                for k in range(3):
                    for l in range(3):
                        recursion(idx+size//3*k,idy+size//3*l,size//3)
                return
    result.append(color)

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

result = []
recursion(0,0,n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))

# Pass