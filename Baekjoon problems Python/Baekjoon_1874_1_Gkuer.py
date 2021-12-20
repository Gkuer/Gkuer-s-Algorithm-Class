import sys
input = sys.stdin.readline

def go():
    t = 1
    arr = []
    ans = []
    while maps:
        a = maps.pop(0)
        if t < a:
            while t <= a:
                arr.append(t)
                ans.append("+")
                t += 1
            arr.pop()
            ans.append("-")
        elif t > a:
            b = arr.pop()
            if a != b:
                return False
            else:
                ans.append("-")
        else:
            t += 1
            ans.append("+")
            ans.append("-")
    return ans

n = int(input())
maps = []
for i in range(n):
    maps.append(int(input()))

res = go()
if res:
    for i in range(len(res)):
        print(res[i])
else:
    print("NO")