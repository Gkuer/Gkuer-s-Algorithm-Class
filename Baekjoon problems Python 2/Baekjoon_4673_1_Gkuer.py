maps = set()
for i in range(1,10001):
    sm = i
    for j in str(i):
        sm += int(j)
    maps.add(sm)

for i in range(1,10001):
    if i not in maps:
        print(i)

# Pass