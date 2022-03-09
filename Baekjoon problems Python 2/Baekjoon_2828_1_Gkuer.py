import sys
input = sys.stdin.readline

n, m = map(int,input().split())
j = int(input())
start = 1
end = start + m - 1

cnt = 0
for i in range(j):
    goal = int(input())
    if start <= goal <= end:
        continue

    elif end < goal:
        cnt += goal - end
        start += goal - end
        end = goal

    elif goal < start:
        cnt += start - goal
        end -= start - goal
        start = goal

print(cnt)

# Pass