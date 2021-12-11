import sys
input = sys.stdin.readline

dict = {}
def w(a,b,c):
    if (a,b,c) in dict:
        return dict[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    if a < b and b < c:
        x, y, z = w(a,b,c-1), w(a,b-1,c-1), w(a,b-1,c)
        dict[(a,b,c-1)], dict[(a,b-1,c-1)], dict[(a,b-1,c)] = x, y, z
        return x + y - z

    i, j, k, l = w(a-1,b,c), w(a-1,b-1,c), w(a-1,b,c-1), w(a-1,b-1,c-1)
    dict[(a-1,b,c)], dict[(a-1,b-1,c)], dict[(a-1,b,c-1)], dict[(a-1,b-1,c-1)] = i, j, k, l
    return i + j + k - l

while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

# Pass