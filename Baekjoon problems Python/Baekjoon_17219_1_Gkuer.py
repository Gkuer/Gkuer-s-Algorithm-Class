import sys
input = sys.stdin.readline

n, m = map(int,input().split())
site_dict = {}
for i in range(n):
    site, password = input().split()
    site_dict[site] = password

for i in range(m):
    query = input().strip()
    print(site_dict[query])

# Pass