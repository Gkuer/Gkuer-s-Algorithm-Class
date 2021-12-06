def pect(x):
    if x <= 1:
        return 1
    return x*pect(x-1)

n, k = map(int,input().split())
if k < 0:
    print(0)
elif k > n:
    print(0)
else:
    print(pect(n)//(pect(k)*pect(n-k)))

# Pass