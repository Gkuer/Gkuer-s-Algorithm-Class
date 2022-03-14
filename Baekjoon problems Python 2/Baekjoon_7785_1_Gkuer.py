import sys
input = sys.stdin.readline

n = int(input())
maps = {}
for i in range(n):
    name, status = input().split()
    maps[name] = status

ans = []
for name, status in maps.items():
    if status == "enter":
        ans.append(name)

for name in sorted(ans,reverse=True):
    print(name)

# Pass