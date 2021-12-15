import sys
input = sys.stdin.readline

n = int(input())
maps = input()

sum = 0
dp = [0] * (n+1)
for i in range(n):
    val = ord(maps[i])-96
    sum += val*(31**i)

print(sum%1234567891)

# Pass