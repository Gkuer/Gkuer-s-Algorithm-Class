n, m = map(int,input().split())
if n > m:
    n, m = m, n

N, M = n, m

while n % m != 0:
    n, m = m, n%m

print(m)
print(N*M//m)

# Pass