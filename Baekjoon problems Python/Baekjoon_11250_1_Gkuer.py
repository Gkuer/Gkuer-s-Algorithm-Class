t = int(input())
for tc in range(t):
    h, w, n = map(int,input().split())
    order = 0
    flag = False
    for i in range(1,w+1):
        for x in range(1,h+1):
            order += 1
            if order == n:
                print(str(x)+str(i).zfill(2))
                flag = True
                break
        if flag:
            break

# Pass