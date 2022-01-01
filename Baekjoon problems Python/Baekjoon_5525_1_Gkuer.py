import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

cnt = 0
ans = 0
pos = 0
while pos + 1 <= m-1:
    if s[pos-1] == "I" and s[pos] == "O" and s[pos+1] == "I":
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
        pos += 1
    else:
        cnt = 0
    pos += 1

print(ans)

# Pass