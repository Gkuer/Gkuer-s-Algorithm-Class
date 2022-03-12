import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

ans = [0 for i in range(n)]
for i in range(n):
    bigger = 0
    for j in range(n):
        if i != j:
            if maps[i][0] < maps[j][0] and maps[i][1] < maps[j][1]:
                bigger += 1

    ans[i] = bigger+1

print(*ans)

# Pass