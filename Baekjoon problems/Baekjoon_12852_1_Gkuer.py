import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
def find(x):
    if dp.get(x):
        return dp[x]

    cnts = []
    records = []
    if x % 3 == 0:
        cnt, record = find(x//3)
        cnts.append(cnt)
        records.append(record)

    if x % 2 == 0:
        cnt, record = find(x//2)
        cnts.append(cnt)
        records.append(record)

    cnt, record = find(x-1)
    cnts.append(cnt)
    records.append(record)

    min_cnt = min(cnts)
    min_record = records[cnts.index(min_cnt)]
    dp[x] = [min_cnt+1,[x]+min_record]
    return [min_cnt+1,[x]+min_record]

n = int(input())
dp = {1:[0,[1]]}
ans = find(n)

print(ans[0])
print(*ans[1])

# Fail: Timeover