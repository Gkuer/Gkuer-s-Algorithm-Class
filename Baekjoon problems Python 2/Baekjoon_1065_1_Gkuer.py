n = int(input())

ans = 0
for i in range(1,n+1):
    temp = str(i)
    if len(temp) <= 1:
        ans += 1
    else:
        ini = int(temp[1]) - int(temp[0])

        for j in range(1,len(temp)-1):
            if int(temp[j+1]) - int(temp[j]) != ini:
                break
        else:
            ans += 1

print(ans)

# Pass