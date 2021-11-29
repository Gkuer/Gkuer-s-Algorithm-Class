import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
cnt = [0] * n
for i in range(n):
    for x in range(i):
        if cnt[x] > cnt[i] and arr[x] < arr[i]:
            cnt[i] = cnt[x]
    cnt[i] += 1
print(max(cnt))
# Pass