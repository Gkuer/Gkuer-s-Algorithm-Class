import sys
input = sys.stdin.readline

def dfs(idx,mode):
    temps = [-1]*(n+1)
    temps[idx] = 0
    q = []
    q.append(idx)
    while q:
        now = q.pop()
        for i in maps[now]:
            if temps[i[0]] == -1:
                temps[i[0]] = temps[now] + i[1]
                q.append(i[0])
    if mode == 1:
        return temps.index(max(temps))
    elif mode == 2:
        return max(temps)

n = int(input())
maps = [[] for _ in range(n+1)]
root_val = 1
for i in range(n):
    temp = list(map(int, input().split()))
    temp_len = len(temp)
    for x in range((temp_len-2)//2):
        maps[temp[0]].append([temp[2*x+1],temp[2*x+2]])

    if temp_len > root_val:
        root = temp[0]
        root_val = temp_len

print(dfs(dfs(root,1),2))

# Pass