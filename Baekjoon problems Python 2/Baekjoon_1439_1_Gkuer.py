import sys
input = sys.stdin.readline

s = input().strip()
cnt = [0,0]
start = 0
while start < len(s):

    while start < len(s)-1 and s[start] == s[start+1]:
        start += 1

    cnt[int(s[start])] += 1
    start += 1

print(min(cnt))

# Pass