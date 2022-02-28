import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1,t+1):
    a, b = map(int, input().split())
    A, B = a, b

    while a%b != 0:
        a, b = b, a%b

    print(A*B//b)

# Pass