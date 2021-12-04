n, m = map(int,input().split())
maps = list(map(int,input().split()))

for i in maps:
    if i < m:
        print(i, end=" ")

# Pass