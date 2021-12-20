import sys
input = sys.stdin.readline

def inorder(root, depth):
    global col
    if root == -1:
        return
    inorder(maps_left[root],depth+1)
    subans[depth].append(col)
    col += 1
    inorder(maps_right[root],depth+1)


n = int(input())
maps_left = [0]*(n+1)
maps_right = [0]*(n+1)
node = [0]*(n+1)
for _ in range(n):
    a, b, c = map(int,input().split())
    maps_left[a], maps_right[a] = b, c
    node[a] += 1
    if b != -1:
        node[b] += 1
    if c != -1:
        node[c] += 1

root = 0
for i in range(1,n+1):
    if node[i] == 1:
        root = i

subans = [[] for _ in range(n+1)]
col = 1
inorder(root,1)

ans = 0
ans_idx = 1
for i in range(1,n+1):
    if subans[i]:
        res = max(subans[i]) - min(subans[i]) +1
        if res > ans:
           ans_idx = i
           ans = res

print(ans_idx,ans)

# Pass
