import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

sosu = []
for i in range(m,n+1):
    for j in range(2,i):
        if not (i % j):
            break
    else:
        sosu.append(i)

if sosu and sosu[0] == 1:
    sosu = sosu[1:]

if sosu:
    print(sum(sosu))
    print(sosu[0])
else:
    print(-1)

# Pass