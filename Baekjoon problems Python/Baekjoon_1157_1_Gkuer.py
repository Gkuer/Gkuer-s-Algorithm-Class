word = input().upper()
sd = {}
for i in word:
    if sd.get(i):
        sd[i] += 1
    else:
        sd[i] = 1

mx = 0
for i,x in sd.items():
    if x > mx:
        mx = x
        mx_idx = i
        cnt = 1
    elif x == mx:
        cnt += 1


print("?") if cnt >= 2 else print(mx_idx.upper())

# Pass