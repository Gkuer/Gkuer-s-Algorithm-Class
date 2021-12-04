import sys
input = sys.stdin.readline

def pactorial(x):
    if x == 1:
        return 1

    return x * pactorial(x-1)

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    if n >= m:
        print(1)
    else:
        print(pactorial(m) // (pactorial(n) * pactorial(m-n)))

# Pass