import sys
input = sys.stdin.readline

n = list(map(int,input().strip()))

n = sorted(n,reverse=True)

for i in n:
    print(i,end="")

# Pass