import sys
input = sys.stdin.readline

def find(pos):
    maps[pos] = 1

    for j in rel_maps[pos]:
        if not maps[j]:
            find(j)

n, m = map(int,input().split())
truths = list(map(int,input().split()))
maps = [0] * (n+1)

rel_maps = [[] for _ in range(n+1)]

pre_ans = []
for _ in range(m):
    temp = list(map(int,input().split()))
    for i in temp[1:]:
        for j in temp[1:]:
            if i != j:
                rel_maps[i].append(j)
    pre_ans.append(temp)

for i in truths[1:]:
    find(i)

cnt = 0
for i in pre_ans:
    for j in i[1:]:
        if not maps[j]:
            break
    else:
        cnt += 1

print(m-cnt)

# Pass