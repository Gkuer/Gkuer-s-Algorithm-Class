import sys
input = sys.stdin.readline

def gcd(n,m):
    while m > 0:
        n, m = m, n%m
    return n

n, m = map(int,input().split())

res_gcd = gcd(max(n,m), min(n,m))
res_lcm = n*m//res_gcd

print(res_gcd)
print(res_lcm)

# Pass