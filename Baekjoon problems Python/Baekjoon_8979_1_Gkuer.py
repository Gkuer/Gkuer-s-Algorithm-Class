import sys
input = sys.stdin.readline

n, k = map(int,input().split())
maps = []

for i in range(n):
    a, b, c, d = input().split()
    maps.append([int(b)*1000000000000 + int(c)*10000000 + int(d),int(a)])

maps.sort(reverse=True)

pre_ans = 0
for i in range(n):
    if maps[i][1] == k:
        pre_ans = maps[i][0]

for i in range(n):
    if maps[i][0] == pre_ans:
        print(i+1)
        break