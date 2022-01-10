import sys
input = sys.stdin.readline

n, r, c = map(int,input().split())

res = -1
while n > 1:
    size = (2**n)//2
    if r < size and c < size:
        pass
    elif r < size and size <= c:
        res += size**2
        c -= size
    elif r >= size and c < size:
        res += (size**2) * 2
        r -= size
    elif r >= size and c >= size:
        res += (size**2) * 3
        r -= size
        c -= size
    n -= 1

flag = False
for i in range(2):
    for j in range(2):
        res += 1
        if i == r and j == c:
            flag = True
            break
    if flag:
        break

print(res)

# Pass