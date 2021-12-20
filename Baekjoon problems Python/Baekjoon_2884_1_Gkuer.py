h, m = map(int,input().split())

next_m = m - 45

if next_m < 0:
    next_m = 60 + next_m
    h -= 1

if h < 0:
    h = 24 + h

print(str(h) + " " + str(next_m))

# Pass