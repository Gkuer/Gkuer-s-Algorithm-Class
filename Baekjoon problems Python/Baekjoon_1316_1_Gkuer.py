import sys
input = sys.stdin.readline

t = int(input())
ans = 0
for _ in range(1,t+1):
    data = input().strip()
    temp = [data[0]]
    pre = data[0]
    for i in data:
        if i == pre:
            continue
        elif i not in temp:
            pre = i
            temp.append(i)
        else:
            break
    else:
        ans += 1

print(ans)