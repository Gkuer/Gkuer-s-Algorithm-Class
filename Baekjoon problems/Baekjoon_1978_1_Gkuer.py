import sys
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        for i in range(2,x):
            if x % i == 0:
                return 0
    return 1

n = int(input())
maps = list(map(int,input().split()))

cnt = 0
while maps:
    a = maps.pop()
    cnt += prime(a)

print(cnt)

# Pass