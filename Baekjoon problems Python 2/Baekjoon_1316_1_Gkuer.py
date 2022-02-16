import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    data = input().strip()
    maps = {}
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            continue
        else:
            if data[i] in maps:
                break
            else:
                maps[data[i]] = 1
    else:
        if data[-1] not in maps:
            ans += 1

print(ans)

# Pass