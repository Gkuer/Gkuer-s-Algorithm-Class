import sys
input = sys.stdin.readline

maps = [0]
for i in range(8):
    maps.append(int(input()))

ans = sorted(maps)[-5:]

sm = 0
sub_ans = []
for i in range(1,9):
    if maps[i] in ans:
      sm += maps[i]
      sub_ans.append(i)

print(sm)
print(*sub_ans)

# Pass