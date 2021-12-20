maps = []
for i in range(10):
    maps.append(int(input()))

ans = set()
for i in range(10):
    ans.add(maps[i] % 42)

print(len(ans))
# Pass