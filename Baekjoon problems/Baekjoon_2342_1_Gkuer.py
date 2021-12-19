import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(now,check):
    if now == 0:
        return 2

    if now == check:
        return 1
    elif (now + check) % 2:
        return 3
    else:
        return 4

def bf(left,right,pos,power):
    global ans

    if maps[pos] == 0:
        if ans > power:
            ans = power
        return

    if power > ans:
        return

    goal = maps[pos]
    bf(goal,right,pos+1,power+check(left,goal))
    bf(left,goal,pos+1,power+check(right,goal))

maps = list(map(int,input().split()))
ans = math.inf
bf(0,0,0,0)
print(ans)

# Fail: Time Over