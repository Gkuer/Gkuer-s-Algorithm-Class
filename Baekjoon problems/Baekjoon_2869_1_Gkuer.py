import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())

day = (V-B) / (A-B)
print(int(day)) if int(day) == day else print(int(day)+1)

# Pass