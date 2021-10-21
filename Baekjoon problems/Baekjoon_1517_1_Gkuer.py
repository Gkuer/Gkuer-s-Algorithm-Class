import sys
input = sys.stdin.readline

n = int(input())
maps = list(map(int,input().split()))

cnt = 0
for i in range(n-1):
    for j in range(n-2,i-1,-1):
        if maps[j] > maps[j+1]:
            maps[j], maps[j+1] = maps[j+1], maps[j]
            cnt += 1
        print(maps)
print(cnt)

# Fail: Time Over