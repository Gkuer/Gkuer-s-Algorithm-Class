import sys
input = sys.stdin.readline

def find(x,y):
    if y == 1:
        return x % c
    temp = find(x, y//2)

    if y % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


a, b, c = map(int,input().split())

print(find(a,b))

# Pass