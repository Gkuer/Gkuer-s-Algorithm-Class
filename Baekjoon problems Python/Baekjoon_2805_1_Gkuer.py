import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = list(map(int,input().split()))

mx = max(maps)
sm = 0
while sm < m:
    mx -= 1
    temp = 0
    for i in maps:
        if i - mx > 0:
            temp += i - mx

    sm = temp

print(mx)

# Fail: Time Over